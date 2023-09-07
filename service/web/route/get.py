"""
service/web/route/get.py
--------------------
Description:

GET 요청 라우팅
"""

import share.share as share

app = share.app

# Root GET
@app.get("/")
def root():
    return {
        "message": "Hello! This is FastAPI"
    }