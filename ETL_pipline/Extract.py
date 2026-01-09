import requests
import time

def fetch_jobData():
    """
    crawler 104 職缺資料
    http get method
    地點: 台中、高雄、台南
    職位: 前端、後端、全端、軟體 工程師
    預設抓取5頁共100個職缺資訊
    """

    count = 1
    jobData = []
    prev = None

    while(count <= 5):
        jobUrl = f"https://www.104.com.tw/jobs/search/api/jobs?area=6001008000%2C6001014000%2C6001016000&jobcat=2007001015%2C2007001016%2C2007001017%2C2007001004&jobsource=index_s&mode=s&page={count}&pagesize=20"
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*",
        "Referer": "https://www.104.com.tw/jobs/"
        }

        for i in range(3):
            try:
                res = requests.get(jobUrl, headers=headers, timeout=30)
                res.raise_for_status()
                prev = res.json()
                break
            except Exception as e:
                print(f"Link fail for {i+1} times: {e}")
                return "Url fail"
                time.sleep(2)

        jobData += prev["data"]
        count+=1

    return jobData
