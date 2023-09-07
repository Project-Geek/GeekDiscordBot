"""
service/web/app.py
--------------------
Description:

fastapi 웹 서비스 시작점
"""

import uvicorn

import share.share as share
from share.config import CONFIG
from fastapi import FastAPI

share.app = FastAPI()

# Route
import service.web.route.get
import service.web.route.post

# Command Call (변경예정)
def stop():
    pass

def start():
    uvicorn.run(share.app, host=CONFIG['web']['host'], port=CONFIG['web']['port'])