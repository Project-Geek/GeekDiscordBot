"""
main.py
--------------------
Description:

프로그램 진입점
"""
from share.config import CONFIG

import service.database as db
import service.web.app as app



# web service 시작함
app.start()
print("!")