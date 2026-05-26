import requests

def board_curing_F4():
    url = 'http://10.3.10.118/api/v1/lh/equip-live-board/'  # 四分厂硫化看板地址
    machine_list = []
    re = requests.get(url)
    print(re.status_code)
    data = re.json()
    data_machine = data.get("data")
    header2 = data.get("headers")
    for i in data_machine:
        num1 = i.get("equip_group")
        for j in header2:
            if j not in i.keys():
                continue
            machine_id = str(num1) + str(j)+'L'
            A_data = i.get(j) or {}  # 数据到机台01,02...
            B_data = A_data.get('L') or {}  # 数据到左右模，取左模

            status = B_data.get('status', 0)
            production = B_data.get("production", 0)
            stop_duration = B_data.get("stop_duration", 0)
            color = B_data.get("color", "#FFFFFF")

            machine_list.append(
                {"id": machine_id, "status": status, "production": production, "stoptime": stop_duration,
                 "color": color})

            machine_id = str(num1) + str(j)+'R'
            C_data = A_data.get('R') or {}  # 数据到左右模，取左模

            status = C_data.get('status', 0)
            production = C_data.get("production", 0)
            stop_duration = C_data.get("stop_duration", 0)
            color = C_data.get("color", "#FFFFFF")

            machine_list.append(
                {"id": machine_id, "status": status, "production": production, "stoptime": stop_duration,
                 "color": color})





    return machine_list


def board_building_F4():
    url = 'http://10.3.10.118/api/v1/cx/equip-live-board/'
    machine_list = []
    re = requests.get(url)
    data1 = re.json().get("data_1")  # 一次发设备
    data2 = re.json().get("data_2")  # 二次法设备
    headers_1 = re.json().get("headers_1")
    headers_2 = re.json().get("headers_2")
    for i in data1:
        num1 = i.get('equip_group')
        for j in headers_1:
            if j not in i.keys():
                continue

            print(j)
            machine_id = str(num1) + str(j)

            A_data = i.get(j) or {}  # 数据到机台01,02...

            status = A_data.get('status', 0)
            production = A_data.get("production", 0)
            stop_duration = A_data.get("stop_duration", 0)
            color = A_data.get("color", "#FFFFFF")

            machine_list.append(
                {"id": machine_id, "status": status, "production": production, "stoptime": stop_duration,
                 "color": color})
    for i in data2:
        num1 = i.get('equip_group')
        for j in headers_2:
            if j not in i.keys():
                continue

            print(j)
            machine_id = str(num1) + str(j)

            A_data = i.get(j) or {}  # 数据到机台01,02...

            status = A_data.get('status', 0)
            production = A_data.get("production", 0)
            stop_duration = A_data.get("stop_duration", 0)
            color = A_data.get("color", "#FFFFFF")

            machine_list.append(
                {"id": machine_id, "status": status, "production": production, "stoptime": stop_duration,
                 "color": color})

    return machine_list


def board_semi_F4():
    url = 'http://10.3.10.118/api/v1/bbj/equip-live-board/'
    machine_list = []
    re = requests.get(url)
    print(re.status_code)
    data = re.json()
    data_machine = data.get("data")
    header2 = data.get("headers")
    for i in data_machine:
        num1 = i.get("equip_group")
        for j in header2:
            if j not in i.keys():
                continue
            machine_id = str(num1) + str(j)
            A_data = i.get(j) or {}  # 数据到机台01,02...

            status = A_data.get('status', 0)
            production = A_data.get("production", 0)
            print(production)
            stop_duration = A_data.get("stop_duration", 0)
            color = A_data.get("color", "#FFFFFF")
            unit = A_data.get("unit", "unit")
            if production != 0:
                production = str(production) + str(unit)
            machine_list.append(
                {"id": machine_id, "status": status, "production": production, "stoptime": stop_duration,
                 "color": color})
    return machine_list



if __name__=="__main__":
    print(board_building_F4())
    print(board_curing_F4())
    print(board_semi_F4())