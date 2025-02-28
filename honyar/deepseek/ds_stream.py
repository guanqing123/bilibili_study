from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)
stream = client.chat(model='deepseek-r1:8b', stream=True, messages=[
    {
        'role': 'system',
        'content': '你是一个乐于助人的助手',
    },
    {
        'role': 'user',
        'content': '9.11和9.9哪个数字大',
    },
])

for chunk in stream:
    print(chunk['message']['content'], end='', flush=True)
