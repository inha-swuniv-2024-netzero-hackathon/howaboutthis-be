import boto3,os

# Creating new record in DynamoDB table

# 만약에 람다에서 안불러와지면 그땐 따로 트러블슈팅 해야 함
client = boto3.client('dynamodb')
# response = client.describe_table(
#     TableName='netzero-team-6-dynamodb-table'
# )

response = client.update_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'item_id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'title',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'description',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'password',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'exchange_status',
            'AttributeType': 'S'
        }
    ],
    TableName='netzero-team-6-dynamodb-table',
    TableClass='STANDARD'
    )
print(response)