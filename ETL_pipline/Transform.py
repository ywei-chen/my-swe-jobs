def transfrom_jobData(jobData):
    transfromed_jobData = []

    for job in jobData:
        each_jobData ={
            # 預留DB的PK
            'id': job.get('custNo', None),

             # 首頁呈現: 公司名稱、職稱、直轄市區、薪資
            'company': job.get('custName', None),
            'name': job.get('jobName', None),
            'addr': job.get('jobAddrNoDesc', None),
            'salary': f"{job.get('salaryLow')} ~ {job.get('salaryHigh')}"
                          if job.get('salaryLow') and job.get('salaryHigh')
                          else "待遇面議",
                          
            # 點擊詳情可顯示: 公司名稱、職稱、具體地址、薪資、工作內容、擅長工具、上班時間、應徵連結
            'description': job.get('description', None),
            'realAddr': f"{job.get('jobAddrNoDesc')}{job.get('jobAddress')}",
            'workingtime': job.get('d3'),
            'skill': '、'.join([s['description'] for s in job.get('pcSkills')]) 
                     if job.get('pcSkills') 
                     else "不拘",
            'link': job.get('link').get('cust')
        }
        
        transfromed_jobData.append(each_jobData)

    return transfromed_jobData