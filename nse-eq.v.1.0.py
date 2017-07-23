import requests
import os
from datetime import datetime, timedelta

def MonthCode(m):
    if m == 1:
        return "JAN"
    elif m == 2:
        return "FEB"
    elif m == 3:
        return "MAR"
    elif m == 4:
        return "APR"
    elif m == 5:
        return "MAY"
    elif m == 6:
        return "JUN"
    elif m == 7:
        return "JUL"
    elif m == 8:
        return "AUG"
    elif m == 9:
        return "SEP"
    elif m == 10:
        return "OCT"
    elif m == 11:
        return "NOV"
    elif m == 12:
        return "DEC"

def DayCode(d):
    if d < 10:
        return "0" + str(d)
    else:
        return str(d)
site = "https://nseindia.com"
home = "D:\\"

def directory(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', 'Connection': 'keep-alive', 'Content-Type': 'application/zip', 'Referer': 'https://www.nseindia.com/products/content/derivatives/equities/archieve_fo.htm', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36', 'X-frame-options': 'SAMEORIGIN'}
cookies = {'pointer':'1','sym1':'KPIT', 'NSE-TEST-1':'1826627594.20480.0000'}


start_date = input("Enter start date (dd-mm-yy): ")
end_date = input("Enter end date (dd-mm-yy): ")

sdate = datetime.strptime(start_date, '%d-%m-%y')
edate = datetime.strptime(end_date, '%d-%m-%y')

delta = timedelta(days=1)

while sdate <= edate:
    print(sdate)
    path = "/content/historical/DERIVATIVES/" + str(sdate.year) + "/" + MonthCode(sdate.month) + "/fo" + DayCode(sdate.day) + MonthCode(sdate.month) + str(sdate.year) + "bhav.csv.zip"
    url = site + path
    print (url)
    req = requests.get(url,headers=headers,cookies=cookies)
    if req.status_code == 200:
        fileName = home + str(sdate.year) + "\\" + MonthCode(sdate.month) + "-" + str(sdate.year) + "\\" + str(sdate.day) + "-" + str(sdate.month) + "-" + str(sdate.year) + ".zip"
        directory(fileName)
        file = open(fileName, 'wb')
        for chunk in req.iter_content(100000):
            file.write(chunk)
        file.close()
        sdate += delta
    else:
        print ("DATA DOES NOT EXIST FOR THIS DATE")
        sdate += delta
    

