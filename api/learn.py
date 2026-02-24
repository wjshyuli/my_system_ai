from fastapi import APIRouter
from scripts.fuck import fucker


router = APIRouter()
@router.get("/hello")
async def hello_world():
    a=fucker()
    return {"message": a}






