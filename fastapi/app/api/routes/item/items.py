from fastapi import FastAPI, APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse

router = APIRouter()


# 상품 등록
@router.post("/api/item")
async def post_item(request: Request):
    # body 파싱
    
    # db.dynamodb 모듈 불러오기
    
    # dynamodb에 게시글 정보 삽입
    return

# 단일 상품 조회
@router.get("/api/item")
async def get_item(request: Request):
    # item_id 를 가지고 dynamodb에서 찾기
    
    # dynamodb 에 존재하는 S3_image_url 가지고 이미지도 가져오기
    
    return

# 상품 리스트 조회
@router.get("/api/item")
async def get_item_list(request: Request):
    
    # dynamodb에서 모든 item 가져오기
    
    # dynamodb 에 존재하는 S3_image_url 가지고 이미지도 가져오기
    
    return

# 상품 수정
@router.patch("/api/item")
async def update_item(request: Request):
    
    # body에 password도 같이 받아오기
    
    # 해당 password가 dynamodb에 저장된 document의 password field랑 동일한지 검증
    
    # 동일하다면 request body의 내용으로 해당 document 수정
    
    return

# 상품 삭제
@router.delete("/api/item")
async def delete_item(request: Request):
    
    # body에 password도 같이 받아오기
    
    # 해당 password가 dynamodb에 저장된 document의 password field랑 동일한지 검증
    
    # 동일하다면 request body의 내용으로 해당 document 삭제
    
    return
