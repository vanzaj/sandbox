from api import client

model = "chatgpt-4o-latest"
prefix = "Once upon a time "
messages = [
    {
    "role": "system",
    "content": "you are a storyteller"
    },
    {"role": "user",
     "content": prefix}
]

response = client.chat.completions.create(model=model, messages=messages, max_tokens=100, stream=True)
print(prefix, end="")
for message in response:
    content = message.choices[0].delta.content
    if content:
        print(content, end="")
