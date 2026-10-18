import httpx

messages = []

while True:
    user_input = input("请输入：").strip()

    if user_input.lower() == "exit":
        break

    if not user_input:
        continue

    messages.append({
        "role" : "user",
        "content" : user_input
    })

    try:
        response = httpx.post(
            "http://127.0.0.1:8000/chat",
            json = {"messages" : messages},
            timeout = 90,
            trust_env = False
        )
        response.raise_for_status()
        reply = response.json()["reply"]
    except (httpx.HTTPError, KeyError, ValueError) as e:
        messages.pop()
        print("请求失败：", e)
        if isinstance(e, httpx.HTTPStatusError):
            print("服务端详情：", e.response.text)
        continue

    print("AI:", reply)

    messages.append({
        "role" : "assistant",
        "content" : reply
    })

