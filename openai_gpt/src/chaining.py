from api import client

model = "chatgpt-4o-latest"

initial_prompt = "Write a concise paragraph about the lyrical characteristics and themes of old-school rap."

messages = [
    {"role": "system", "content": "You are an expert music critic."},
    {"role": "user", "content": initial_prompt},
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=200,
    temperature=0.5,
    stop=["assistant:", "user:"],
)

about_old_school_rap = response.choices[0].message.content

new_rap_song_prompt = f"Context: {about_old_school_rap} Task: Create lyrics for an old-school rap song about justice and equality."

messages = [
    {"role": "system", "content": "You are a popular old-school rap lyricist."},
    {"role": "user", "content": new_rap_song_prompt}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    max_tokens=500,
    temperature=1,
    stop=["assistant:", "user:"],
)

new_song = response.choices[0].message.content

print(f"Prompt that was fed into the model:\n{new_rap_song_prompt}\n")
print(f"Result:\n{new_song}\n")
