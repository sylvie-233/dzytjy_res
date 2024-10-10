from fastapi import FastAPI

from routes.fileroute import fileRoute
from models.databases import create_all_tables

app = FastAPI()

create_all_tables()
app.include_router(fileRoute)




