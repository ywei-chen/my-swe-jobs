from ETL_pipline import Extract, Transform, Load
from DB import testconnection, operation

# crawler職缺資料並清洗資料
raw_data = Extract.fetch_jobData()
transed_data = Transform.transform_jobData(raw_data)

# 測試DB連線
db_test = testconnection.test_connection()

# DB table 新建 & 更新
operation.create_table()

# load 清洗後的資料 into DB
load_db = Load.load_to_db(transed_data)

# 創建job_list API endpoint 需要的列表資料
operation.replace_view()