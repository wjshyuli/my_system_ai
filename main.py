from fastapi import FastAPI, Request
import threading
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from api.api import router as api_router
from api.learn import router as learn_router
from api.jodoo import router as jodoo_router
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.staticfiles import StaticFiles
from scripts.get_mes_board import fetch_mes_data


app = FastAPI(title="My")

# 注册API路由
app.include_router(api_router, prefix="/api")
app.include_router(learn_router, prefix="/learn")
app.include_router(jodoo_router, prefix="/jodoo")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模板目录
templates = Jinja2Templates(directory="templates")


# 首页
@app.get("/ai")
async def home(request: Request):
    return templates.TemplateResponse("ai.html", {"request": request})


@app.on_event("startup")
def start_fetch_mes_data():
    # 后台线程执行，不阻塞 FastAPI
    t = threading.Thread(target=fetch_mes_data, daemon=True)
    t.start()