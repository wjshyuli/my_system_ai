from fastapi import APIRouter,Request,Header, HTTPException
from fastapi.templating import Jinja2Templates
from scripts.get_mix_code_info import get_mix_code_info


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/get_mix_code")
def get_mix_code(code: str, Authorization: str = Header(None)):
    token = Authorization.replace("Bearer ", "")
    return get_mix_code_info(code, token)











# from fastapi import APIRouter, Header, HTTPException, Depends
#
# router = APIRouter()
#
# # 依赖函数（统一鉴权）
# def get_token_from_header(token: str = Header(None, alias="Authorization")) -> str:
#     """
#     从 Authorization header 拿 token 并去掉 Bearer 前缀
#     """
#     if not token:
#         raise HTTPException(status_code=401, detail="缺少token")
#
#     return token.replace("Bearer ", "")
# #
# # # 接口
# # @router.get("/get_mix_code")
# # def get_mix_code(code: str, token: str = Depends(get_token_from_header)):
# #     """
# #     token 会自动被依赖函数解析
# #     """
# #     return get_mix_code_info(code, token)