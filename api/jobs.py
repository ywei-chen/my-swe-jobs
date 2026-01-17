from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, ConfigDict
from typing import Optional
from DB.testconnection import Session
from DB.models import Job

"""
Jobs API
職缺資料相關的 API 端點
"""
app = FastAPI(title="Job_API", description="Job_DATA")

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["http://localhost:5173"],
    allow_methods=["*"]
)


# 用於Job_detail的資料格式
class JobDetail_response(BaseModel):
    id: int
    company: Optional[str] = None
    name: Optional[str] = None
    addr: Optional[str] = None
    salary: Optional[str] = None
    description: Optional[str] = None
    realAddr: Optional[str] = None
    workingtime: Optional[str] = None
    skill: Optional[str] = None
    link: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

# 用於Job_list的資料格式
class JobList_response(BaseModel):
    id: int
    company: Optional[str] = None
    name: Optional[str] = None
    addr: Optional[str] = None
    salary: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)



def get_db():
    with Session() as db:
        yield db

@app.get(
    "/jobs/{job_id}", 
    response_model= JobDetail_response,
    summary="取得所有職缺的詳細資料",
    description="回傳詳細的職缺資料，用於單一職缺詳情"
    )
def get_per_jobsDetail(job_id: int, db = Depends(get_db)):
    jobs = db.query(Job).filter(Job.id == job_id).first()
    if jobs is None:
        raise HTTPException(status_code=404, detail=f"無相關資料")
    return jobs


@app.get(
    "/jobs",
    response_model= list[JobList_response],
    summary="取得所有職缺的部分資料",
    description="回傳部分的職缺資料，用於職缺列表頁"
)
def get_all_jobsList(db = Depends(get_db)):
    jobs = db.query(
        Job.id,
        Job.company,
        Job.name,
        Job.addr,
        Job.salary
    ).order_by(Job.id.asc())
    return jobs
