import boto3

region_name = 'eu-west-1'

table_name = 'studentXtable' #change X to your student number

def get_client():
    return boto3.client('dynamodb', region_name=region_name)

def get_item(table, key):
    client = get_client()
    response = client.get_item(
        TableName=table,
        Key=key
    )
    return response['Item']

def get_items(table, keys):
    client = get_client()
    response = client.batch_get_item(
        RequestItems = {
            table: {
                'Keys': keys
            }
        }
    )
    return response['Responses'][table_name]

'''Getting one item using key'''
print('Getting one item from a table')
key = {
        'Id': {'N': '3'},
        'Name': {'S': 'Elon Musk'}
      }
item = get_item(table_name, key)
print('Item: {0}'.format(item))

'''Getting more than one item using keys'''
print('Getting two items from a table')
keys = [
            {
                'Id': {'N': '3'},
                'Name': {'S': 'Elon Musk'}
            },
            {
                'Id': {'N': '2'},
                'Name': {'S': 'Jeff Bezos'}
            }
]

items = get_items(table_name, keys)
print('Items: {0}'.format(items))
