import boto3

QUEUE_NAME = 'my queue name'
REGION = 'eu-west-1'

def get_sqs():
    sqs = boto3.resource('sqs', region_name=REGION)
    return sqs

def delete_messages(queue_name):
    sqs = get_sqs()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    for message in queue.receive_messages(MaxNumberOfMessages=1):
        print('{0}'.format(message.body))
        print('Deleting message')
        message.delete()

delete_messages(QUEUE_NAME)
