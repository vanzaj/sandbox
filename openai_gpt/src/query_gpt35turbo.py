from api import client

model = "gpt-3.5-turbo"

messages = [
    {
    "role": "system",
    "content": "You are a smart and creative assistant."
    },
    {"role": "user",
     "content": "Who is Michael Jackson"}
]

response = client.chat.completions.create(model=model, messages=messages, max_tokens=50)
print(response.usage)
print("---"*10)

print("Short answer:", response.choices[0].message.content)
print("---"*10)

response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
print("Long answer: ", response.choices[0].message.content)
print("---"*10)

response = client.chat.completions.create(model=model, messages=messages, max_tokens=100, stop=["."])
print("Stop answer: ", response.choices[0].message.content + ".")