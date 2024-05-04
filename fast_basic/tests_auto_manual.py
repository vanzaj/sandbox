import requests


print(requests.get("http://127.0.0.1:8000").json())

print(requests.get("http://127.0.0.1:8000/items/0").json())

print(requests.get("http://127.0.0.1:8000/items/1001").json())

print(requests.get("http://127.0.0.1:8000/items?name=Nails").json())

print(requests.get("http://127.0.0.1:8000/items?category=tools").json())
