# AI Chatbot

基于 FastAPI 和 DeepSeek API 开发的 AI 聊天机器人。

这是我的第一个 Python 后端开发项目，主要用于实践 HTTP API、异步编程、大模型调用及 Git 版本管理。

## 1. 项目功能

- 基于 FastAPI 构建后端服务
- 通过 DeepSeek API 实现 AI 对话
- 支持多轮聊天和上下文记忆
- 使用 httpx 发送异步 HTTP 请求
- 使用 Pydantic 验证请求数据
- 使用 .env 管理 API Key
- 实现基本的异常处理
- 通过命令行客户端进行交互

## 2. 技术栈

- Python
- FastAPI
- Uvicorn
- HTTPX
- Pydantic
- DeepSeek API
- Git / GitHub

## 3. 项目结构

ai-chatbot/
├── main.py             # FastAPI 服务端
├── client.py           # 命令行聊天客户端
├── requirements.txt    # 项目依赖
├── .env                # API Key（不上传）
├── .gitignore          # Git 忽略规则
└── README.md           # 项目说明

## 4. 安装与运行

### ① 克隆项目

git clone https://github.com/lanyanyayaya-byte/ai-chatbot.git

cd ai-chatbot

### ② 创建虚拟环境

python3 -m venv .venv

source .venv/bin/activate

### ③ 安装依赖

pip install -r requirements.txt

### ④ 配置 API Key

在项目根目录创建 .env 文件，填写：

DEEPSEEK_API_KEY=你的API_Key

注意：不要将真实 API Key 上传到 GitHub。

### ⑤ 启动服务端

uvicorn main:app --reload

默认运行地址：

http://127.0.0.1:8000

API 文档：

http://127.0.0.1:8000/docs

### ⑥ 启动客户端

新建一个终端，激活虚拟环境，然后执行：

python client.py

输入消息即可开始聊天。

输入 exit 退出程序。

## 5. API 接口

### POST /chat

请求示例：

{
    "messages": [
        {
            "role": "user",
            "content": "你好"
        }
    ]
}

响应示例：

{
    "reply": "你好！有什么可以帮助你的吗？"
}

## 6. 实现原理

用户输入消息
    ↓
client.py 发送 HTTP 请求
    ↓
FastAPI 接收并验证 JSON
    ↓
服务端调用 DeepSeek API
    ↓
DeepSeek 返回模型回答
    ↓
FastAPI 返回 JSON
    ↓
客户端显示回答并保存聊天记录

多轮对话通过 messages 列表保存历史消息实现。

## 7. 后续计划

- [x] FastAPI 后端搭建
- [x] DeepSeek API 接入
- [x] 基本异常处理
- [x] 多轮聊天
- [ ] 流式输出
- [ ] 网页聊天界面
- [ ] SQLite 聊天记录存储
- [ ] Docker 部署

## 8. 项目说明

本项目主要用于学习 Python 后端开发及大模型应用开发，目前为个人学习项目。