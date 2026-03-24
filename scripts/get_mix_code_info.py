import requests

VALID_TOKENS = {"A7K9X2M4Q1"}

def get_mix_code_info(code, token):

    if token not in VALID_TOKENS:
        return {"message": "你无权查询此信息"}

    try:
        r = requests.get(
            f'http://10.3.10.65/openapi/pallet-instorage/?YCLCODE={code}',
            timeout=20
        )
        r.raise_for_status()
        data = r.json()
        if data["success"] == False:
            return {'message':'Can not find this code'}
        else:
            return data



    except requests.exceptions.RequestException as e:
        return {"error": f"请求失败: {str(e)}"}


if __name__ == '__main__':
    a = get_mix_code_info('ZCTHA0220260324144234D984', 'A7K9X2M4Q1')
    print(a)