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
