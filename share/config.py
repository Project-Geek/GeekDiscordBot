"""
share/config.py
--------------------
Description:

config 파일에 대한 정보를 가져오는 부분
민감한 부분은 제거해야 하나? -> 더 좋은 방법이 있다면 수정
"""

import yaml

CONFIG_FILE = "./config/config.yaml"

# 변동 없는 놈이니 상수화 함
with open(CONFIG_FILE, "r") as f:
    CONFIG = yaml.load(f, Loader=yaml.FullLoader)