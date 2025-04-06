
import urllib.parse
import boto3
import json
import io
import logging
import datetime

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# AWS Clients
s3 = boto3.client('s3')
textract = boto3.client('textract')
comprehend = boto3.client('comprehend')
bedrock = boto3.client('bedrock-runtime')

def lambda_handler(event, context):
    bucket_name = "resume-analyzer-container"
    file_name = "Pranamika Paul_Cloud_Backend_AWS_AI_Engineer.png"
    
    # Metadata for logs
    request_id = context.aws_request_id
    timestamp = datetime.datetime.utcnow().isoformat()

    logger.info(f"[{timestamp}] 🚀 Lambda invoked | Request ID: {request_id}")
    logger.info(f"[{timestamp}] 📂 Using hardcoded file key: {file_name}")

    try:
        # Step 1: Get file from S3
        logger.info(f"[{timestamp}] 📦 Fetching file from S3 bucket: {bucket_name}")
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = file_obj['Body'].read()

        # Step 2: Extract text using Textract
        logger.info(f"[{timestamp}] 🧠 Extracting text with Textract...")
        text = extract_text_with_textract(bucket_name, file_name)
        logger.info(f"[{timestamp}] ✅ Text extraction complete. Length: {len(text)} characters")

        # Step 3: Analyze text with Comprehend
        logger.info(f"[{timestamp}] 🔍 Running NLP analysis with Amazon Comprehend...")
        response = comprehend.detect_entities(Text=text, LanguageCode="en")
        logger.info(f"[{timestamp}] ✅ NLP analysis complete. Entities found: {len(response['Entities'])}")

        # Step 4: Generate AI feedback using Bedrock
        logger.info(f"[{timestamp}] 🤖 Sending text to Bedrock for feedback generation...")
        ai_feedback = generate_resume_feedback(text)
        logger.info(f"[{timestamp}] ✅ Bedrock feedback received.")

        # Final result log
        logger.info(f"[{timestamp}] ✅ Lambda completed successfully.")

        return {
            "resume_text": text,
            "skills": response["Entities"],
            "feedback": ai_feedback
        }

    except s3.exceptions.NoSuchKey:
        logger.error(f"[{timestamp}] ❌ File not found in S3 bucket '{bucket_name}' with key '{file_name}'")
        raise

    except Exception as e:
        logger.error(f"[{timestamp}] ❌ Unexpected error: {str(e)}")
        raise

def extract_text_with_textract(bucket, document_key):
    """Use Amazon Textract to extract text from an image/PDF stored in S3."""
    response = textract.detect_document_text(
        Document={
            'S3Object': {
                'Bucket': bucket,
                'Name': document_key
            }
        }
    )
    text = ""
    for item in response["Blocks"]:
        if item["BlockType"] == "LINE":
            text += item["Text"] + "\n"
    return text

def generate_resume_feedback(text):
    """Generate AI-based resume feedback using Amazon Bedrock (Anthropic Claude)."""
    body = {
        "prompt": f"\n\nHuman:Analyze this resume and provide improvement suggestions:\n\n{text}\n\nAssistant:",
        "max_tokens_to_sample": 200,
        "temperature": 0.7
    }

    response = bedrock.invoke_model(
        modelId="anthropic.claude-v2:1",
        contentType="application/json",
        accept="application/json",
        body=json.dumps(body)
    )

    result = json.loads(response["body"].read())
    return result.get("completion", "No feedback generated.")
