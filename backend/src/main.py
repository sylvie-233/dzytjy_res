from fastapi import FastAPI

from routes.fileroute import fileRoute
from models.databases import create_all_tables

app = FastAPI()

# 根据模型创建所有表
# create_all_tables()

# 导入子路由
app.include_router(fileRoute)




