### IAM Role for Lambda: resumeAnalyzer_pranamika-role-wwaawdnz

- AWS Managed Type

- AmazonS3ReadOnlyAccess
- AmazonLexFullAccess
- AWSLambda_FullAccess

- Customer inline

- AccessBedRock
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "bedrock:InvokeModel",
                "Resource": "arn:aws:bedrock:us-west-2::foundation-model/anthropic.claude-v2:1"
            }
        ]
    }

- AllowComprehend
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "comprehend:DetectSentiment",
                "comprehend:DetectEntities",
                "comprehend:DetectSyntax",
                "comprehend:DetectKeyPhrases"
            ],
            "Resource": "*"
        }
    ]
}

- AllowTextractDetect
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": "textract:DetectDocumentText",
            "Resource": "*"
        }
    ]
}

- Get_Object_From_S3
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": "arn:aws:s3:::resume-analyzer-container/*"
        }
    ]
}


- Customer Managed

- AWSLambdaBasicExecutionRole-72569c61-a053-42da-a685-5e214dc5820e
    {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:us-west-2:124355655208:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:us-west-2:124355655208:log-group:/aws/lambda/resumeAnalyzer_pranamika:*"
            ]
        }
    ]
}
