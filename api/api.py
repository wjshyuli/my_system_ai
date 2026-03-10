from fastapi import APIRouter
from scripts.tool_example import run_tool
from scripts.getnews import getnews_of_rubber,getnews_of_gov
from scripts.get_mes_four import mes_four_checkone_result

router = APIRouter()

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


@router.get("/run-script")
def run_script():
    result = run_tool()
    return {"result": result}