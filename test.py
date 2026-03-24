import requests

BASE_URL = "http://127.0.0.1:8053/get_mix_code"
TOKEN = "A7K9X2M4Q1"
CODE = "ZCTHA0220260324144234D984"

response = requests.get(
    BASE_URL,
    headers={"Authorization": f"Bearer {TOKEN}"},
    params={"code": CODE},
    timeout=10
)

print(response.json())