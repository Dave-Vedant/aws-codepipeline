import json 

def lambda_handler(event, context):
    print('request: {}'.format(json.dumps(event)))
    return {
        'statusCode': 200,
        'headers': {
            'content-Type': 'text/plain'
        },
        'body': 'Hello from lambda created via cdk pipeline'
    }