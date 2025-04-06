
# 🤖 AI-Powered Resume Analyzer using AWS Lambda, AWS Bedrock, Textract & Comprehend

A cloud-native serverless project built entirely on the **AWS Free Tier**, this application extracts resume content from images or PDFs uploaded to an S3 bucket and analyzes them using **Amazon Textract**,**Amazon Lambda**, **Amazon Comprehend**, and **Amazon Bedrock** (Claude v2) to generate AI-driven resume improvement feedback. Accessible and scalable!

---

## 🔍 Project Summary

This project helps job seekers enhance their resumes by:
- Extracting text from uploaded resumes (including images)
- Identifying skills and entities
- Generating intelligent suggestions for improvement using AI

🛠 Built with **AWS Lambda**, **S3**, **Textract**, **Comprehend**, **Bedrock**, and optionally **Amazon Lex** for chatbot interaction.

---

## 🧠 Key Features

| Feature             | Technology Used               |
|---------------------|-------------------------------|
| Text Extraction     | 🟡 Amazon Textract            |
| Entity Detection    | 🔵 Amazon Comprehend           |
| Resume Suggestions  | 🟣 Amazon Bedrock (Claude v2) |
| Resume Storage      | 🟢 Amazon S3                  |
| Processing Logic    | ⚙️ AWS Lambda (Python 3.9)    |
| Interaction (opt)   | 💬 Amazon Lex Chatbot         |

---

## 🧩 Architecture Diagram

![AI Resume Analyzer Architecture](./architecture_diagram.png)

---

## 🖥️ Lambda Function - Core Logic

Here’s a simplified view of what happens in the code:

1. **Triggered by File Upload** to S3 bucket.
2. Uses **Textract** to extract lines of text from the resume.
3. Sends extracted text to **Comprehend** to detect skills and entities.
4. Passes text to **Amazon Bedrock (Claude)** to generate AI-powered suggestions.
5. Returns structured output: raw text, list of skills, and tailored feedback.

> 💡 File processed in your current code: `"Pranamika Paul_Cloud_Backend_AWS_AI_Engineer.png"`

---

## 💻 How to Deploy (Step-by-Step)

### 🪜 Step 1: Set Up AWS Free Tier
- Create AWS account.
- Create IAM user with access to:
  - S3, Lambda, Textract, Comprehend, Bedrock, and optionally Lex

### 🪜 Step 2: Create an S3 Bucket
- Name it: `resume-analyzer-container`
- Uncheck "Block Public Access"
- Enable upload event notifications (optional)

### 🪜 Step 3: Create Lambda Function
- Runtime: Python 3.9
- Upload `lambda_function.py` (provided)
- Give permission to access S3, Textract, Comprehend, Bedrock
- Add S3 as an **event trigger**

### 🪜 Step 4: Connect API Gateway (optional)
- Create REST API
- POST method → triggers Lambda
- Deploy and get endpoint URL

### 🪜 Step 5: Optional Lex Bot Integration
- Create chatbot that invokes Lambda for natural language feedback interaction

---

## 🔗 Live Endpoints (Optional)

If you've exposed it via API Gateway:

```
POST Add your Link 
Example:- https://your-api-id.execute-api.region.amazonaws.com/resume
```

---

## 📸 Screenshots

> Add these manually after deployment:
- ✅ [Lambda Console with function logs](Lambda_console_logs.png)
- ✅ [Bedrock invocation example](BedRock_Invocation.png)
- ✅ [Comprehend output screenshot](Comprehend_output.png)
- ✅ [S3 bucket upload trigger UI](s3_trigger.png)![BedRock_Invocation](https://github.com/user-attachments/assets/a3e7a755-34f2-4374-844e-aa3fc83076bc)
![Comprehend_output](https://github.com/user-attachments/assets/6a8511aa-1834-4729-93e1-b99a06c27036)


---

## 🧪 Sample Output

```json
{
  "resume_text": "Experienced Cloud Engineer with AWS & DevOps background...",
  "skills": [
    { "Text": "AWS", "Type": "ORGANIZATION" },
    { "Text": "DevOps", "Type": "OTHER" }
  ],
  "feedback": "You can improve your resume by detailing certifications and quantifying project impact..."
}
```

---

## 📁 Folder Structure

```
📦 AWS-Resume-Analyzer
 ┣ 📄 infrastructure/
 ┣ 📄 lambda/resumeAnalyzer_pranamika/lambda_funtion.py
 ┣ 📄 outputs/
 ┣ 🖼️ architecture_diagram.png
 ┣ 📄 README.md
 ┣ 📄 deployment-checklist.md
 ┣ 📄 resumeAnalyzer_pranamika.yaml
 ┣ 📄 sample-event.json
 ┣ 📄 README.md
 ┗ 📄 requirements.txt (optional)
```

---

## 🚀 Future Improvements

- Add resume upload form using a front-end (React or HTML)
- Chatbot using Amazon Lex
- Store results in DynamoDB
- Multi-language support

---

## 👩‍💻 Author

**Pranamika Paul**  
Cloud | Backend | AWS AI Engineer

🔗 [GitHub Profile](https://github.com/Pranamika-CodeMania/AWS_AI__Powered_Resume_Analyzer)  
📧 Connect on [LinkedIn](https://www.linkedin.com/in/pranamika-paul-holding-valid-emirates-id-087288141/)


## 📁 Lambda Code
Code is located in `lambda/lambda_function.py`.


🔧 Tools & AWS Services Used (All in Free Tier):

Service	Purpose
Amazon S3	Store uploaded resumes
AWS Lambda	Backend code to extract and process resume content
Amazon Comprehend	Natural Language Processing (NLP) to extract key skills/entities
Amazon Bedrock	Uses Claude AI to generate resume improvement suggestions
Amazon Lex	Creates an interactive chatbot for resume feedback
API Gateway	Creates an HTTP endpoint to trigger resume processing
IAM	Securely control permissions across services

⚙️ Workflow Summary

Upload Resumes → to S3

Trigger Lambda Function → Extract text using Textract

Use Comprehend → Analyze and extract key information

Compare & Rank → Matching against job description based on extracted skills

Store Results → In a database

Display Output → Via API or UI dashboard

✅ Benefits

Reduces HR screening workload

Ensures skill-based candidate shortlisting

Highly scalable and low-code-friendly using AWS services
