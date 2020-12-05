import boto3
import hashlib

QUEUE_NAME = 'my queue name'
REGION = 'eu-west-1'

def get_sqs():
    sqs = boto3.resource('sqs', region_name=REGION)
    return sqs

def send_messages(queue_name):
    sqs = get_sqs()
    queue = sqs.get_queue_by_name(QueueName=queue_name)

    message_content = 'Duplication test'
    message_group_id = 'Group1'
    message_deduplication_id = '{0}{1}'.format(message_group_id, message_content)
    response = queue.send_message(MessageBody=message_content, MessageGroupId='Group1', MessageDeduplicationId=hashlib.md5(message_deduplication_id.encode('utf-8')).hexdigest())
    print('First request. Message Content: {0}, HTTP Status Code: {1}'.format(message_content, response['ResponseMetadata']['HTTPStatusCode']))
    message_group_id = 'Group2'
    message_deduplication_id = '{0}{1}'.format(message_group_id, message_content)
    response = queue.send_message(MessageBody=message_content, MessageGroupId='Group2', MessageDeduplicationId=hashlib.md5(message_deduplication_id.encode('utf-8')).hexdigest())
    print('Second request. Message Content: {0}, HTTP Status Code: {1}'.format(message_content, response['ResponseMetadata']['HTTPStatusCode']))

send_messages(QUEUE_NAME)
