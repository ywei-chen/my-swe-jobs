from ETL_pipline import Extract, Transform

data = Extract.fetch_jobData()
test = Transform.transfrom_jobData(data)


for i, job in enumerate(test, start=1):
    print(f"{i}.{job['company']}_ {job['name']}_ {job['addr']}")