import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Visitors')

def get_current_count():
    response = table.query(
        KeyConditionExpression=Key('id').eq(0)
    )

    item = response['Items']
    return int(item[0]['count_current_visitors'])
    
def update_item():
    current_count = get_current_count()
    new_count = current_count + 1

    table.update_item(
        Key={
            'id': 0,
            'visitor_counter': 0
        },
        UpdateExpression='SET count_current_visitors = :val1',
        ExpressionAttributeValues={
            ':val1': new_count
        }
    )
    
def lambda_handler(event, context):
    update_item()
    
    return {
        'statusCode': 200,
        'body': 'Success: Database updated.'
    }