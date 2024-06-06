from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_TOKEN"))

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a programming assistant, skilled in Python."},
    {"role": "user", "content": "Generate an example of mocking random() in a unit test"}
  ]
)

print(completion.choices[0].message)
