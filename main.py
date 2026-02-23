from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.example import router as example_router

app = FastAPI(title="My Script Platform")

# 注册API路由
app.include_router(example_router, prefix="/api")

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 模板目录
templates = Jinja2Templates(directory="templates")


# 首页
@app.get("/ai")
def home(request: Request):
    return templates.TemplateResponse("ai.html", {"request": request})


# 测试接口
@app.get("/ping")
def ping():
    return {"message": "pong"}