import boto3
from boto3.dynamodb.conditions import Key, Attr

region_name = 'eu-west-1'

table_name = 'studentXtable' #change X to your student number

def query(address):
    dynamodb = boto3.resource('dynamodb', region_name=region_name)
    table = dynamodb.Table(table_name)
    response = table.query(
            IndexName='Address-index',
            #FilterExpression='attribute_exists(Hobby)',
            KeyConditionExpression=Key('Address').eq(address)
        )
    return response

items = query('Teligi')
print(items)
