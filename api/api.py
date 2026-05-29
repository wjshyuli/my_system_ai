from fastapi import APIRouter
from scripts.tool_example import run_tool
from scripts.getnews import getnews_of_rubber,getnews_of_gov
from scripts.get_mes_four import mes_four_checkone_result
from board_date.last_board_data import last_board_data
from fastapi import Request
from fastapi.templating import Jinja2Templates
import requests
from board_date import last_board_data
from scripts.get_mes_board_F4 import board_semi_F4 ,board_building_F4,board_curing_F4
from scripts.get_mes_board_F1 import board_semi_F1 ,board_building_F1,board_curing_F1
from scripts.get_mes_board_F3 import board_semi_F3 ,board_building_F3,board_curing_F3

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/news_of_rubber")
def news_of_rubber():
    result=getnews_of_rubber()
    return result
@router.get("/mes_four_yijian")
def get_mes_four_yijian():
    result=mes_four_checkone_result()
    return result



@router.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}


@router.get("/mes_board_semi")
def get_mes_board_semi(request: Request):
    result = []
    data=last_board_data
    return templates.TemplateResponse("mes_board_semi.html", {
        "request": request,
        "devices": data
    })

@router.get("/mes_board_building")
def get_mes_board_semi(request: Request):
    result = []
    data=last_board_data
    return templates.TemplateResponse("mes_board_building.html", {
        "request": request,
        "devices": data
    })

@router.get("/mes_board_curing")
def get_mes_board_semi(request: Request):
    result = []
    data=last_board_data
    return templates.TemplateResponse("mes_board_curing.html", {
        "request": request,
        "devices": data
    })

@router.get("/mes_board_semi_dingding")
def get_mes_board_semi_d(request: Request):

    try:

        data_list,s_list=board_semi_F1()





        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_semi = data_list

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_semi


    return templates.TemplateResponse(
        "mes_board_semi_dingding.html",
        {
            "request": request,
            "list": data_list,   # 👈 关键：传给前端
            "s_list": s_list   # 👈 关键：传给前端
        })

@router.get("/mes_board_building_dingding")
def get_mes_board_building_d(request: Request):

    try:

        data_list ,s_list = board_building_F1()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_semi = data_list

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_semi


    return templates.TemplateResponse(
        "mes_board_building_dingding.html",
        {
            "request": request,
            "list": data_list,   # 👈 关键：传给前端
            "s_list": s_list
        })

@router.get("/mes_board_curing_dingding")
def get_mes_board_curing_d(request: Request):
    try:

        data_list , s_list = board_curing_F1()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_semi = data_list

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_semi


    return templates.TemplateResponse(
        "mes_board_curing_dingding.html",
        {
            "request": request,
            "list": data_list ,  # 👈 关键：传给前端
            "s_list": s_list   # 👈 关键：传给前端
        })
@router.get("/mes_board_building3_dingding")
def get_mes_board_dingding_building3(request: Request):
    try:

        data_list,s_list= board_building_F3()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_building3 = data_list
        print(data_list)

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_semi

    return templates.TemplateResponse(
        "mes_board_building3_dingding.html",
        {
            "request": request,
            "list": data_list , # 👈 关键：传给前端
            "s_list": s_list  # 👈 关键：传给前端
        })


@router.get("/mes_board_curing3_dingding")
def get_mes_board_dingding_building3(request: Request):
    try:

        data_list ,s_list = board_curing_F3()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_curing3 = data_list
        print(data_list)

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_curing3

    return templates.TemplateResponse(
        "mes_board_curing3_dingding.html",
        {
            "request": request,
            "list": data_list , # 👈 关键：传给前端
            "s_list": s_list  # 👈 关键：传给前端
        })

@router.get("/mes_board_semi4_dingding")
def get_mes_board_semi4_dingding(request: Request):
    try:

        data_list,status_list = board_semi_F4()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_curing3 = data_list
        print(data_list)

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_curing3

    return templates.TemplateResponse(
        "mes_board_semiF4_dingding.html",
        {
            "request": request,
            "list": data_list,  # 👈 关键：传给前端
            "status_list": status_list  # 👈 关键：传给前端
        })

@router.get("/mes_board_building4_dingding")
def get_mes_board_building4_dingding(request: Request):
    try:

        data_list,status_list = board_building_F4()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_curing4 = data_list


    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_curing4




    return templates.TemplateResponse(
        "mes_board_buildingF4_dingding.html",
        {
            "request": request,
            "list": data_list,  # 👈 关键：传给前端
            "status_list": status_list ,
        })

@router.get("/mes_board_curing4_dingding")
def get_mes_board_curing4_dingding(request: Request):
    try:

        data_list,status_list = board_curing_F4()

        if data_list:  # 👈 关键！！！
            last_board_data.last_board_data_curing3 = data_list
        print(data_list)

    except Exception as e:
        print("接口错误:", e)
        data_list = last_board_data.last_board_data_curing3

    return templates.TemplateResponse(
        "mes_board_curingF4_dingding.html",
        {
            "request": request,
            "list": data_list,  # 👈 关键：传给前端
            "status_list": status_list,  # 👈 关键：传给前端
        })