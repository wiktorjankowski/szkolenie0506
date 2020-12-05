import boto3

QUEUE_NAME = 'my queue name'
REGION = 'eu-west-1'

def get_sqs():
    sqs = boto3.resource('sqs', region_name=REGION)
    return sqs

def send_messages(queue_name):
    sqs = get_sqs()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    for i in range(1,5):
        message_content = 'G1_{0}'.format(i)
        queue.send_message(MessageBody=message_content, MessageGroupId='Group1')

    for i in range(1,3):
        message_content = 'G2_{0}'.format(i)
        queue.send_message(MessageBody=message_content, MessageGroupId='Group2')

send_messages(QUEUE_NAME)
