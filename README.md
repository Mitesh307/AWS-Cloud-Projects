# ⚡ ServerlessNotify — Cloud-Native File Processing & Notification System

A serverless, event-driven cloud project built on AWS that automatically sends email notifications when a file is uploaded to cloud storage.

---

## 🏗️ Architecture

```
User → CloudFront → S3 (File Upload) → Lambda (Auto Triggered) → SNS → Email Notification
                         ↑
                      EC2 (Nginx Web Server)
```

---

## ☁️ AWS Services Used

| Service | Purpose |
|---|---|
| **EC2** | Ubuntu server running Nginx web server |
| **S3** | Stores uploaded files + hosts static frontend |
| **Lambda** | Auto-triggered on S3 upload, processes the event |
| **CloudFront** | CDN for fast and secure HTTPS delivery |
| **SNS** | Sends real-time email notifications |

---

## 🔄 How It Works

1. User visits the static website served via **CloudFront**
2. A file is uploaded to the **S3** bucket
3. S3 triggers the **Lambda** function automatically
4. Lambda reads the filename and bucket name from the event
5. Lambda publishes a notification to **SNS**
6. **SNS** sends an email alert instantly

---

## 📸 Screenshots

### EC2 Nginx Server Running
![EC2](screenshots/ec2-nginx.png)

### S3 Bucket with Uploaded Files
![S3](screenshots/s3-bucket.png)

### Lambda Function with S3 Trigger
![Lambda](screenshots/lambda-trigger.png)

### SNS Topic with Confirmed Subscription
![SNS](screenshots/sns-subscription.png)

### Email Notification Received
![Email](screenshots/email-notification.png)

### CloudFront Live Website
![CloudFront](screenshots/cloudfront-website.png)

---

## 🧠 Lambda Function Code

```python
import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client('sns')
    
    bucket = event['Records'][0]['s3']['bucket']['name']
    filename = event['Records'][0]['s3']['object']['key']
    
    sns.publish(
        TopicArn='arn:aws:sns:ap-south-1:267334620491:serverlessnotify-topic',
        Message=f'New file uploaded! Bucket: {bucket}, File: {filename}',
        Subject='ServerlessNotify - New File Upload!'
    )
    
    return {'statusCode': 200, 'body': 'Notification sent!'}
```

---

## 🚀 Deployment Steps

### 1. EC2 Setup
- Launch t2.micro Ubuntu instance (Free Tier)
- Install and configure Nginx
- Create custom HTML landing page

### 2. S3 Setup
- Create S3 bucket
- Enable static website hosting
- Configure bucket policy for public access
- Upload index.html

### 3. SNS Setup
- Create SNS topic
- Subscribe email address
- Confirm subscription via email

### 4. Lambda Setup
- Create Python 3.12 Lambda function
- Add S3 trigger (PUT event)
- Attach AmazonSNSFullAccess policy
- Deploy the function code

### 5. CloudFront Setup
- Create CloudFront distribution
- Point origin to S3 website endpoint
- Enable HTTPS delivery

---

## 💰 Cost

This project runs entirely on **AWS Free Tier** — $0/month for the first 12 months.

| Service | Free Tier |
|---|---|
| EC2 t2.micro | 750 hrs/month |
| S3 | 5GB storage |
| Lambda | 1M requests/month |
| CloudFront | 1TB transfer/month |
| SNS | 1M notifications/month |

---

## 👨‍💻 Author

**Mitesh Baikar**  
Cloud & DevOps Enthusiast  
[LinkedIn](https://www.linkedin.com/in/mitesh-baikar-3004a22a0/) | [GitHub](https://github.com/Mitesh307)
