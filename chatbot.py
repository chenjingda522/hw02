from openai import OpenAI

# 初始化客户端（DeepSeek 兼容 OpenAI 接口）
client = OpenAI(
    api_key="sk-e06448c1fac2462cb41ec523b0fc66a5y",  # 替换为你的 DeepSeek API Key
    base_url="https://api.deepseek.com"
)

def chat_with_deepseek(user_input):
    """调用 DeepSeek 模型并返回回复"""
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "user", "content": user_input}
        ],
        stream=False
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    print("DeepSeek Chatbot 已启动！输入 'quit' 退出。")
    while True:
        user_input = input("\n你：")
        if user_input.lower() == "quit":
            print("再见！")
            break
        reply = chat_with_deepseek(user_input)
        print(f"\nDeepSeek：{reply}")
