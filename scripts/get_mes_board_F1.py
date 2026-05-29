import time,requests
from board_date.last_board_data import last_board_data
from logs.logger import get_logger
from scripts.get_mes_board_F4 import board_building_F4

logger = get_logger(__name__)


def board_semi_F1():
    res = requests.post(
        "http://10.3.10.61:18080/WebDDIApi/queryBzp",
        timeout=8
    )
    data = res.json()
    data_list = data.get("Object", [])
    s_list = {}
    for item in data_list:
        statues = item["state"]

        if statues not in s_list:
            s_list[statues] = {
                "count": 0,
                "color": item["color"],
            }
        s_list[statues]["count"] += 1
        if item['color'].upper() in ["#FFFFFF", "WHITE","#FFFFF0"]:
            s_list[statues]["color"] ='#000000'


    return data_list,s_list


def board_building_F1():
    res = requests.post(
        "http://10.3.10.61:18080/WebDDIApi/queryCx",
        timeout=8
    )
    data = res.json()
    data_list = data.get("Object", [])
    s_list = {}
    for item in data_list:
        statues = item["state"]

        if statues not in s_list:
            s_list[statues] = {
                "count": 0,
                "color": item["color"],
            }
        s_list[statues]["count"] += 1
        if item['color'].upper() in ["#FFFFFF", "WHITE","#FFFFF0"]:
            s_list[statues]["color"] ='#000000'



    return data_list,s_list

def board_curing_F1():
    res = requests.post(
        "http://10.3.10.61:18080/WebDDIApi/queryLh",
        timeout=8
    )
    data = res.json()
    data_list = data.get("Object", [])
    s_list = {}
    for item in data_list:
        statues = item["state"]

        if statues not in s_list:
            s_list[statues] = {
                "count": 0,
                "color": item["color"],
            }

        s_list[statues]["count"] += 1
        if item['color'].upper() in ["#FFFFFF", "WHITE","#FFFFF0"]:
            s_list[statues]["color"] ='#000000'



    return data_list,s_list


if __name__ == "__main__":
    a,b = board_building_F1()
    print(a)
    print(b)