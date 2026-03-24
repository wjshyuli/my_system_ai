from fastapi import APIRouter

from fastapi import Request
from fastapi.templating import Jinja2Templates
from scripts.get_mix_code_info import get_mix_code_info


router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/get_mix_code")
def get_mix_code(code:str,token:str):
    result=  get_mix_code_info(code,token)
    return result