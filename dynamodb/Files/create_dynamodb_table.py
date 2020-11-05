import boto3

region_name = 'eu-west-1'

table_name = 'studentXtable' #change X to your student number

def create_dynamodb_table(table):
    client =  boto3.client('dynamodb', region_name=region_name)
    response = client.create_table(
        TableName=table,
        AttributeDefinitions=[
            {
                'AttributeName': 'Id',
                'AttributeType': 'N' #'S'|'N'|'B'
            },
            {
                'AttributeName': 'Name',
                'AttributeType': 'S'
            }
        ],
        KeySchema=[
            {
                'AttributeName': 'Id',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'Name',
                'KeyType': 'RANGE'
            }
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    print(response)

create_dynamodb_table(table_name)
