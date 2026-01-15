from DB.models import Base
from DB.testconnection import engine, Session, DB_URL

"""
CRUD與操作DB的各項函式
"""

def create_table():
    Base.metadata.create_all(engine)
    print("創建jobs table成功")