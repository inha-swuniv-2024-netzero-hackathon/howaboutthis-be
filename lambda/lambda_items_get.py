
from typing import Optional
from pydantic import BaseModel
import boto3, json

# AWS DynamoDB 연결
dynamodb_client = boto3.client('dynamodb')
s3 = boto3.client('s3')

def get_dynadb_item(author_slack_id, upload_unixtime, dynamodb_client):
    
    table_name = 'netzero-team-6-dynamodb-table'  # 삽입할 테이블의 이름
    
    response = dynamodb_client.get_item(
    Key={
        'author_slack_id': {
            'S': author_slack_id,
        },
        'upload_unixtime': {
            'S': upload_unixtime,
        },
    },
    TableName=table_name,
    )
    
    response_json = {
        'title': response['Item']['title']['S'],
        'unixtime': response['Item']['upload_unixtime']['S'],
        's3_img_url': response['Item']['s3_image_url']['S'],
        'status': response['Item']['exchange_status']['S'],
        'description' : response['Item']['description']['S'],
    }
    
    return response_json

def get_dynadb_item_list(dynamodb_client):
    result = []
    
    table_name = 'netzero-team-6-dynamodb-table'
    
    # DynamoDB에서 모든 아이템 가져오기
    response = dynamodb_client.scan(TableName = table_name)
    items = response.get('Items', [])

    for item in items:
        title = item.get('title', {}).get('S')
        created_at = item.get('createdAt', {}).get('S')
        status = item.get('status', {}).get('S')
        author_slack_id = item.get('author_slack_id', {}).get('S')
        upload_unixtime = item.get('upload_unixtime', {}).get('S')
        s3_img_url = item.get('s3_image_url', {}).get('S')

        result.append({
            'author_slack_id': author_slack_id,
            'upload_unixtime': upload_unixtime,
            'title': title,
            'createdAt': created_at,
            's3_img_url': s3_img_url,
            'status': status
        })

    result_json = {
        "items": result
    }
    
    return result_json
    
    

# 단일 상품 조회
def get_item(
    author_slack_id: Optional[str],
    upload_unixtime: Optional[str]
):
    if author_slack_id is None and upload_unixtime is None:
        return get_dynadb_item_list(dynamodb_client)
    
    return get_dynadb_item(author_slack_id, upload_unixtime, dynamodb_client) # S3 image url도 내부 field로 존재




# 상품 등록
def lambda_handler(event, context):
    # 이벤트 객체 로그 출력
    print("Received event: " + json.dumps(event, indent=2))
    # 본문(body) 추출
    query_params = event.get('queryStringParameters', {})
    
    author_slack_id = query_params.get('author_slack_id')
    upload_unixtime = query_params.get('upload_unixtime')
    
    if author_slack_id is None and upload_unixtime is None:
        print("get all of items")
        return get_dynadb_item_list(dynamodb_client)
    else:
        return get_dynadb_item(author_slack_id, upload_unixtime, dynamodb_client) # S3 image url도 내부 field로 존재
    


