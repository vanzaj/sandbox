import os
from dotenv import load_dotenv
load_dotenv()
token = os.getenv("SANDBOX_TOKEN")
print(token)
