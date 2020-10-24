import json
import boto3
import os

s3Client = boto3.client('s3')
snsClient = boto3.client('sns', region_name='eu-west-1')

phone_number = os.environ['phone_number']
sender_id = os.environ['sender_id']
topic_name = os.environ['topic_name']
email = os.environ['email']

def lambda_handler(event, context):
    print(json.dumps(event))
    number = phone_number
    send_sms = snsClient.publish(PhoneNumber=number, Message='Generating link')

    check_topics, arn_prefix = list_topics()
    if topic_name not in check_topics:
        topic_response = snsClient.create_topic(Name = topic_name)
        topic_arn = topic_response['TopicArn']  
        print(f'Created topic: {topic_response}')
        email_sub_answer = snsClient.subscribe(TopicArn = topic_arn,Protocol = 'email',Endpoint = email)
        print(f'Status of subcription for email: {email_sub_answer}')
    if topic_name in check_topics:
        print(f'Found topic: {topic_name}')
        constructed_arn = arn_prefix + ':' + topic_name
        
        for record in event['Records']:
            bucket_name = record['s3']['bucket']['name']
            print(bucket_name)
            file_name = record['s3']['object']['key']
            print(file_name)
            url = s3Client.generate_presigned_url('get_object', Params = {'Bucket': bucket_name, 'Key': file_name}, ExpiresIn = 3600)
            print(url)
            response = snsClient.publish(TopicArn=constructed_arn, Message=url)
            print(f'Response from SNS: {response}')
        
def list_topics():
    topics = snsClient.list_topics()
    topic_list = topics['Topics']
    if not topic_list:
        return [],[]
    topic_names = [t['TopicArn'].split(':')[5] for t in topic_list]
    arn_prefix = ":".join(topic_list[0]['TopicArn'].split(":", 5)[:5])
    print(arn_prefix)
    return topic_names, arn_prefix
