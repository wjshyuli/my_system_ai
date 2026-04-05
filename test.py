import requests

res = requests.post(
    "http://10.3.10.61:18080/WebDDIApi/queryBzp",
    timeout=8
)
data = res.json()
data_list = data.get("Object", [])

print(data_list)