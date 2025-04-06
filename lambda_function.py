import urllib.parse
import boto3
import json
import io
import logging

# Logging setup
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

    try:
        logger.info(f"📂 Using hardcoded file key: {file_name}")

        # Fetch file from S3
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_name)
        file_content = file_obj['Body'].read()

        # Extract text using Textract
        text = extract_text_with_textract(bucket_name, file_name)

        # Analyze with Comprehend
        response = comprehend.detect_entities(Text=text, LanguageCode="en")

        # Generate feedback using Bedrock
        ai_feedback = generate_resume_feedback(text)

        return {
            "resume_text": text,
            "skills": response["Entities"],
            "feedback": ai_feedback
        }

    except s3.exceptions.NoSuchKey:
        logger.error(f"❌ File not found in S3 bucket '{bucket_name}' with key '{file_name}'")
        raise

    except Exception as e:
        logger.error(f"❌ Unexpected error: {str(e)}")
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


