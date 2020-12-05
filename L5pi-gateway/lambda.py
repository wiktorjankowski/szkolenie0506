import json
def lambda_handler(event, context):

    print(json.dumps(event))

    return {
        "statusCode": 200,
        "body": json.dumps('Cheers from AWS Lambda!!'),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
            },
    }
