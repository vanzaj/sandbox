from api import client

model = "chatgpt-4o-latest"


def single_query():
    messages = [
        {"role": "system", "content": "you are an expert XP developer"},
        {
            "role": "user",
            "content": "Describe common code smells using Python code as examples",
        },
    ]

    response = client.chat.completions.create(model=model, messages=messages)

    print(response.choices[0].message.content)


def multiple_query():
    messages = [
        {"role": "system", "content": "you are an expert XP developer"},
        {
            "role": "user",
            "content": "Describe the meaning of Collective Code Ownership",
        },
    ]

    response = client.chat.completions.create(
        model=model, messages=messages, n=2, stop=["\n"]
    )
    for choice in response.choices:
        print(f"Choice:{choice.index}")
        print(choice.message.content)
        print()


if __name__ == "__main__":
    multiple_query()
