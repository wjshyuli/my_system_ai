from fastapi import APIRouter
from scripts.tool_example import run_tool
from scripts.getnews import getnews_of_rubber,getnews_of_gov

router = APIRouter()

@router.get("/news_of_rubber")
def news_of_rubber():
    result=getnews_of_rubber()
    return result


@router.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}


@router.get("/run-script")
def run_script():
    result = run_tool()
    return {"result": result}