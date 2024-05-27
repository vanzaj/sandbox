import base64
from dotenv import load_dotenv
from github import Github
import os

load_dotenv()
access_token = os.getenv("SANDBOX_TOKEN")
g = Github(access_token)

repo = g.get_repo("vanzaj/sandbox")

contents = repo.get_contents("")
while contents:
    file = contents.pop(0)
    if file.type == "dir":
        contents.extend(repo.get_contents(file.path))
    else:
        print(file)

