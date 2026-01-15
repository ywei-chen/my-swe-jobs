from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Text, Integer

Base = declarative_base()
"""
DB TABLE Model
"""

class Job(Base):
    __tablename__ = "jobs"

    # PK主鍵
    id = Column(Integer, primary_key=True, autoincrement=True, comment='編號')

    # 首頁基本資訊
    company = Column(String(50), comment='公司名稱')
    name = Column(String(50), comment='職位名稱')
    addr = Column(String(10), comment='地區')
    salary = Column(String(20), comment='薪資範圍')

    # 內部詳細資訊
    description = Column(Text, comment='工作內容')
    realAddr = Column(String(500), comment="完整地址")
    workingtime = Column(String(500), comment="上班時間")
    skill = Column(String(500), comment="所需技能")
    link = Column(String(500), comment="應徵連結")

