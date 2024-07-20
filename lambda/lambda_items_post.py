import json
import boto3

# AWS DynamoDB 연결
dynamodb_client = boto3.client('dynamodb')
s3 = boto3.client('s3')

def dynadb_insert_item(body, dynamodb_client):
    author_slack_id = body['author_slack_id']
    upload_unixtime = body['upload_unixtime']
    title = body['title']
    description = body['description']
    password = body['password']
    exchange_status = body['exchange_status']
    s3_image_url = body['s3_image_url']
    
    # 테이블 이름 설정
    table_name = 'netzero-team-6-dynamodb-table'
    
    # 삽입할 데이터 정의
    item = {
        'author_slack_id': {'S': author_slack_id},
        'upload_unixtime': {'S': upload_unixtime},
        'title': {'S': title},
        'description': {'S': description},
        'password': {'S': password},
        'exchange_status': {'S': exchange_status},
        's3_image_url': {'S': s3_image_url}
    }
    
    # 데이터 삽입
    try:
        response = dynamodb_client.put_item(
            TableName=table_name,
            Item=item
        )
        print("Insert succeeded")
        return "Insert succeeded"
    except Exception as e:
        print("Error inserting item:", e)
        return str(e)

# 상품 등록
def lambda_handler(event, context):
    # 이벤트 객체 로그 출력
    print("Received event: " + json.dumps(event, indent=2))
    
    
    # 본문(body)이 JSON 형식으로 제공되는 경우, 파싱
    try:
        body_data = event
    except json.JSONDecodeError:
        body_data = {}
        print("Error parsing JSON from body")
    
    response_message = dynadb_insert_item(body_data, dynamodb_client)
    
    return {
        'statusCode': 200,
        'body': json.dumps({"message": response_message})
    }
