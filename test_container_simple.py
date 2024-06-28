import requests

url = 'http://localhost:9000/test'
n = 10

response = requests.post(url, json={"number": n}).json()
print(response)