"""
example.py
--------------------
Description:

각종 사용 예제들을 모아놓은 곳이다.
"""

# Database
import service.database as db

# db 연결함
db.connect()

#--------------------------------
# 쿼리 테스트 (users 테이블 있어야댐)
print("==== Example Query Test ====")
rows, count = db.execute("SELECT * FROM users;")
# rows 나 count 가 None 이면 잘못된거임
assert rows is not None
print("length :", count)
for row in rows:
    print(row)

# 값 집어넣음
rows, _ = db.execute("INSERT INTO users (`name`) VALUES ('안뇽');")
assert rows is not None

print("#")
# 잘뜨나 확인 ㄱ
rows, count = db.execute("SELECT * FROM users;")
assert rows is not None
print("length :", count)
for row in rows:
    print(row)

db.close()
db.connect()
#--------------------------------
# 롤백 테스트
print("==== Example Execute & Rollback Test ====")
# 추적 시작
db.begin()

# 값 집어넣음
rows, _ = db.execute("INSERT INTO users (`name`) VALUES ('반영이될까?');")
assert rows is not None

# 롤백함
db.rollback()

# 잘뜨나 확인 ㄱ
rows, count = db.execute("SELECT * FROM users;")
assert rows is not None
print("length :", count)
for row in rows:
    print(row)

# 닫음
db.close()

# 롤백안되누 고쳐봄