from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.api import router as api_router
from api.learn import router as learn_router

app = FastAPI(title="My")

# 注册API路由
app.include_router(api_router, prefix="/api")
app.include_router(learn_router, prefix="/learn")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模板目录
templates = Jinja2Templates(directory="templates")


# 首页
@app.get("/ai")
async def home(request: Request):
    return templates.TemplateResponse("ai.html", {"request": request})

