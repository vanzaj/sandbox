from api import client

model = "chatgpt-4o-latest"
prefix = "\n\n"
messages = [
    {
    "role": "system",
    "content": "you are an expert XP developer"
    },
    {"role": "user",
     "content": "Describe common code smells using Python code as examples"}
]

response = client.chat.completions.create(model=model, messages=messages)

print(response.choices[0].message.content)
