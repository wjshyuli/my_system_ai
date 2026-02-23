from fastapi import APIRouter
from scripts.tool_example import run_tool

router = APIRouter()


@router.get("/hello")
def say_hello():
    return {"message": "Hello FastAPI"}


@router.get("/run-script")
def run_script():
    result = run_tool()
    return {"result": result}