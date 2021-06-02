import DataCloner

def lambda_handler(event, context):
    cloner = DataCloner.DataCloner()
    cloner.cloneCsvData()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
