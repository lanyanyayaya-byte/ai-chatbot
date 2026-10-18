import os
import httpx

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

load_dotenv()
API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = "https://api.deepseek.com/chat/completions"

app = FastAPI()


class Message(BaseModel):
    role : Literal["user", "assistant"]
    content : str

class ChatRequest(BaseModel):
    messages:list[Message]

class ChatResponse(BaseModel):
    reply:str

async def ask_ai(messages : list[Message]):
    if not API_KEY:
        raise HTTPException(
            status_code = 500,
            detail = "没有配置API_KEY"
        )
    headers = {
        "Authorization" : f"Bearer {API_KEY}"
    }

    data = {
        "model" : "deepseek-flash",
        "messages" : [
            *[msg.model_dump() for msg in messages]
        ]
    }

    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                API_URL,
                headers=headers,
                json=data
            )
            response.raise_for_status()
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="大模型请求超时"
        )
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=502,
            detail=f"大模型接口错误：{e.response.status_code}"
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="无法连接大模型服务器"
        )

    result = response.json()

    try:
        reply = result["choices"][0]["message"]["content"]
        if not isinstance(reply, str):
            raise ValueError("回答格式错误")
    except(KeyError, IndexError, TypeError, ValueError):
        raise HTTPException(
            status_code = 502,
            detail = "大模型返回的数据格式异常"
        )
    return reply

@app.post("/chat", response_model=ChatResponse)
async def chat(request:ChatRequest):
    if (not request.messages 
        or request.messages[-1].role != "user"
        or not request.messages[-1].content.strip()):
        raise HTTPException(
            status_code = 400,
            detail = "最后一条消息必须是非空的用户信息"
        )

    reply = await ask_ai(request.messages)
    return {"reply" : reply}