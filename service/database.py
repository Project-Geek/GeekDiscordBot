"""
service/database.py
--------------------
Description:

database 관련 코드 여기서 일괄 처리
대부분 편리하게 alias 함수 콜 형식으로 구현
DB 다른거 사용해도 다 통하게 만들면 댐
"""
from share.config import CONFIG
import pymysql

conn = None
cur  = None

def connect():
    global conn, cur
    conn = pymysql.connect(host=CONFIG['database']['host'], \
                    port=CONFIG['database']['port'], \
                    user=CONFIG['database']['user'], \
                    password=CONFIG['database']['password'], \
                    db=CONFIG['database']['db'], \
                    charset='utf8')
    # Connection Complete
    cur = conn.cursor()
    
# sql 실행 바로 적용
def query(sql):
    cur, rowcount = execute(sql)
    commit()
    return cur, rowcount

def execute(sql):
    try:
        cur.execute(sql)
        return cur, cur.rowcount
    except Exception as e:
        print("Database Execute ERROR :", e)
        return None, None

# sql 실행 후 commit 대기
def begin():
    conn.begin()

# 대기중 처리 모두 적용
def commit():
    conn.commit()

# 대기중 처리 모두 철회
def rollback():
    conn.rollback()

# connection 닫음
def close():
    conn.close()