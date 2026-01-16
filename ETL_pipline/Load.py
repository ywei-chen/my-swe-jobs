from DB.models import Job
from DB.testconnection import Session
from sqlalchemy import text

def load_to_db(transformed_jobData, clear_data =True):
    """
    將trasform.py轉成dist後的資料轉成DB Model的格式
    1. 先刪除舊資料
    2. 重置PK(job_id)
    3. 存入新資料到DB中
    """
    with Session() as db:
        try:
            if clear_data:
                delete_count = db.query(Job).delete()
                print(f"已刪除舊資料: 共{delete_count}筆")

                restart_job_id = """
                    ALTER SEQUENCE jobs_id_seq RESTART WITH 1
                """
                db.execute(text(restart_job_id))
                print("已重置 job_id sequence")

            jobs = []
            for job_data in transformed_jobData:
                job = Job(**job_data)
                jobs.append(job)

            db.add_all(jobs)
            db.commit()
            print("資料存入成功")
            return True
        
        except Exception as e:
            db.rollback()
            print(f"資料存入失敗: {e}")
            return False