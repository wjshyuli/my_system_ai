import requests
from datetime import datetime,timedelta
import pandas as pd


#用俞立的账号去获取jwt token
def get_authorization(user='1001247',pwd='zc123456'):
    url = "http://10.3.10.118/api/v1/user/login/"
    data = { "username": user, "password": pwd}
    headers = { "Content-Type": "application/json"}
    r = requests.post(url, json=data, headers=headers)
    token=r.json().get('token')
    auth='JWT '+token
    return auth

#拿去四分厂外观检测标的昨天一天的外观一检登记的数据
def get_data_checkone(st,et,auth):

    url = "http://10.3.10.118/api/v1/quality/qc-first-check-report/"



    params = {
        "page": "1",
        "page size": "20",
        "st": st,
        "et":et,
        "qc_type":"1",
    }
    headers = {
        "Authorization": auth,
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"}
    r = requests.get(url, params=params,headers=headers )
    r=r.json()
    return r

def mes_four_checkone_result():
    auth = get_authorization()
    et = str(datetime.now().replace(hour=7, minute=0, second=0, microsecond=0))
    st = str(datetime.now().replace(hour=7, minute=0, second=0, microsecond=0) - timedelta(days=1))
    data=get_data_checkone(st,et,auth)
    df = pd.DataFrame(data)
    df = df[["spec_name", "fault_code", "quantity"]]

    # 1 总病疵
    result1 = {
        "title": "昨日总病疵数",
        "data": int(df["quantity"].sum())
    }

    # 2 规格排行
    spec_rank = df.groupby("spec_name")["quantity"].sum().sort_values(ascending=False).head(5).reset_index()
    result2 = {
        "title": "规格问题排行",
        "data": spec_rank.to_dict('records')
    }


    # 3 病疵排行
    fault_rank = df.groupby("fault_code")["quantity"].sum().sort_values(ascending=False).head(5).reset_index()

    result3 = {
        'title':'病疵排行',
        'data': fault_rank.to_dict('records')
    }

    # # 4 规格×病疵矩阵 生成一个矩阵，然并卵
    # pivot = pd.pivot_table(df, values="quantity", index="spec_name", columns="fault_code", aggfunc="sum", fill_value=0)
    top10 =df.groupby(["spec_name","fault_code"])["quantity"].sum().sort_values(ascending=False).head(10).reset_index()
    result4 = {
        'title':'规格病疵排行',
        'data': top10.to_dict('records')
    }
    return result1,result2,result3,result4





if __name__=="__main__":
    mes_four_checkone_result()
    r1,r2,r3,r4 = mes_four_checkone_result()
    print(r1)
    print(r2)
    print(r3)
    print(r4)