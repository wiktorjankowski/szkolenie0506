import boto3

QUEUE_NAME = 'my queue name'
REGION = 'eu-west-1'

def get_sqs():
    sqs = boto3.resource('sqs', region_name=REGION)
    return sqs

def read_messages(queue_name):
    sqs = get_sqs()
    queue = sqs.get_queue_by_name(QueueName=queue_name)
    print('First request')
    #for message in queue.receive_messages(MaxNumberOfMessages=2, WaitTimeSeconds=20):
    for message in queue.receive_messages(MaxNumberOfMessages=2):
        print('{0}'.format(message.body))

    print('Second request')
    for message in queue.receive_messages(MaxNumberOfMessages=2):
        print('{0}'.format(message.body))

read_messages(QUEUE_NAME)
