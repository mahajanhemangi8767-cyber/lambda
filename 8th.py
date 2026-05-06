import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

def lambda_handler(event, context):

    params = event.get('queryStringParameters') or {}

    user_id = params.get('user_id')
    email = params.get('email')

    if not user_id or not email:
        return {
            'statusCode': 400,
            'body': json.dumps("Missing user_id or email")
        }

    table.put_item(
        Item={
            'user_id': user_id,
            'email': email
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps("User stored successfully")
    }
