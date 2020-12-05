import boto3

QUEUE_NAME = 'my queue name'
REGION = 'eu-west-1'

def get_sqs():
    sqs = boto3.resource('sqs', region_name=REGION)
    return sqs

def send_messages(queue_name):
    sqs = get_sqs()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    message_content = 'Duplication test'
    response = queue.send_message(MessageBody=message_content, MessageGroupId='Group1')
    print('First request. Message Content: {0}, HTTP Status Code: {1}'.format(message_content, response['ResponseMetadata']['HTTPStatusCode']))
    response = queue.send_message(MessageBody=message_content, MessageGroupId='Group2')
    print('Second request. Message Content: {0}, HTTP Status Code: {1}'.format(message_content, response['ResponseMetadata']['HTTPStatusCode']))

send_messages(QUEUE_NAME)
