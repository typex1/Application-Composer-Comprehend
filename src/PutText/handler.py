import json
import os
import boto3

table_name = os.environ['TEXTTABLE_TABLE_NAME']
topic_arn = os.environ ['TEXTTOPIC_TOPIC_ARN']

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)

comprehend_client = boto3.client('comprehend')
sns_client = boto3.client('sns')

def handler(event, context) :
    # Log the event argument for debugging and for use in local development.
    print(json.dumps(event))

    text=json.loads(event['body'])['text']
    # Detect sentiment
    response = comprehend_client.detect_sentiment(
        Text = text,
        LanguageCode = 'en'
    )
    sentiment = response['Sentiment']
    
    # Publish message
    sns_client.publish(TopicArn=topic_arn, Message=f'Text {text} got the sentiment {sentiment}.', Subject='New Entry!')
    table.put_item(Item={'text': text, 'sentiment': sentiment})
    
    return {
        'statusCode': 200,
        'body': f'Success with {sentiment} sentiment'
    }
