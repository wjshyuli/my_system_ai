from fastapi import APIRouter
from scripts.tool_example import run_tool
from scripts.getnews import getnews_of_rubber,getnews_of_gov
from scripts.get_mes_four import mes_four_checkone_result
from date.last_board_data import last_board_data
from fastapi import Request
from fastapi.templating import Jinja2Templates


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