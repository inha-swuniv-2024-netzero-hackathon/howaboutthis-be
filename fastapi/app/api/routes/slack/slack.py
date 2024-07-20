from fastapi import FastAPI, HTTPException
import requests
from pydantic import BaseModel

app = FastAPI()

SLACK_BOT_TOKEN = 'xoxb-7448488439683-7442066677862-GgtYBKb24XbDffS6cKQmtxaE'

class DMRequest(BaseModel):
    user_a_id: str
    user_b_id: str
    text: str

def open_dm(user_ids):
    url = 'https://slack.com/api/conversations.open'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
    }
    data = {
        'users': user_ids
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200 and response.json().get('ok'):
        channel_id = response.json().get('channel', {}).get('id')
        if channel_id:
            return channel_id
        else:
            raise HTTPException(status_code=500, detail="Failed to get channel ID")
    else:
        raise HTTPException(status_code=500, detail="Failed to open DM channel")

def send_message(channel_id, text):
    url = 'https://slack.com/api/chat.postMessage'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {SLACK_BOT_TOKEN}'
    }
    data = {
        'channel': channel_id,
        'text': text
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code != 200 or not response.json().get('ok'):
        raise HTTPException(status_code=500, detail="Failed to send message")

@app.post("/api/slack/connect")
def create_and_send(request: DMRequest):
    try:
        # DM 채널 생성
        dm_channel_id = open_dm(f"{request.user_a_id},{request.user_b_id}")
        
        # 메시지 전송
        send_message(dm_channel_id, request.text)
        
        return {"dm_channel_id": dm_channel_id, "detail": "Message sent successfully"}
    except HTTPException as e:
        raise e
