import openai

# 设置你的GPT-3 API密钥
api_key = "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"

# 初始化OpenAI客户端
openai.api_key = api_key

print("欢迎来到ChatGPT对话！输入'退出'以结束对话。")

# 初始化对话历史
conversation_history = []

while True:
    # 获取用户输入
    user_input = input("祁果: ")

    # 退出循环
    if user_input.lower() == '退出':
        print("对话结束。")
        break

    # 将用户输入添加到对话历史中
    conversation_history.append({"role": "user", "content": user_input})

    # 调用GPT-3进行回复
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )

    # 从GPT-3的回复中提取文本
    bot_reply = response.choices[0].message["content"]

    # 将机器人回复输出并添加到对话历史中
    print("ChatGPT:", bot_reply)
    conversation_history.append({"role": "assistant", "content": bot_reply})
