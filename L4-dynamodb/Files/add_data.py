import boto3

region_name = 'eu-west-1'

table_name = 'studentXtable' #change X to your student number

item = {
    'Id': {'N': '1'},
    'Name': {'S': 'Elon Musk'}
}

def get_client():
    
    return boto3.client('dynamodb', region_name=region_name)

'''
Adding one item to the table
'''
def add_item_to_dynamodb_table(table, item):
    client =  get_client()
    response = client.put_item(TableName=table, Item=item)
    print(response)

'''
Adding an array of items to the table
'''
def add_items_to_dynamodb_table(table):
    client =  get_client()
    response = client.batch_write_item(RequestItems=
        {table :
            [
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '2'},
                        'Name': {'S': 'Jeff Bezos'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '3'},
                        'Name': {'S': 'Elon Musk'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '4'},
                        'Name': {'S': 'Albert Einstain'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '5'},
                        'Name': {'S': 'Isaac Newton'},
                        'Address': {'S': 'Westminster Abbey'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '6'},
                        'Name': {'S': 'Michal Adamkiewicz'},
                        'Address': {'S': 'Teligi'},
                        'Hobby': {'S': 'AWS'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '7'},
                        'Name': {'S': 'Isaac Newton'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '8'},
                        'Name': {'S': 'Isaac Newton'},
                        'Hobby': {'S': 'Apples'}
                    }
                }
            },
            {
                'PutRequest' : {
                    'Item' : {
                        'Id': {'N': '9'},
                        'Name': {'S': 'Isaac Newton'},
                        'Address': {'S': 'Teligi'}
                    }
                }
            }
    ]})
    print(response)

add_item_to_dynamodb_table(table_name, item)
add_items_to_dynamodb_table(table_name)
