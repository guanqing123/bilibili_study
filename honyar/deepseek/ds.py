from ollama import Client

client = Client(
    host='http://localhost:11434',
    headers={'x-some-header': 'some-value'}
)
# ollama ls
response = client.chat(model='deepseek-r1:8b', messages=[
    {
        'role': 'system',
        'content': '你是一个乐于助人的助手',
    },
    {
        'role': 'user',
        'content': '你叫什么名字',
    },
])
print(response['message']['content'])
