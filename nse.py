import requests
import os
from datetime import datetime, timedelta


def FindDays(month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 31
    if month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    if year % 4 == 0:
        return 29
    else:
        return 28

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

#url = 'https://www.nseindia.com/content/historical/DERIVATIVES/2016/AUG/fo10AUG2016bhav.csv.zip'

site = "https://www.nseindia.com"
home = "D:\\"


def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def directory(f):
    d = os.path.dirname(f)
    if not os.path.exists(d):
        os.makedirs(d)

start_date = input("Enter start date (dd/mm/yyyy): ")
end_date = input("Enter end date (dd/mm/yyyy): ")

sdate = datetime.strptime(start_date, '%d-%m-%y')
edate = datetime.strptime(end_date, '%d-%m-%y')

delta = timedelta(days=1)

while sdate <= edate:
    path = "/content/historical/DERIVATIVES/" + str(sdate.year) + "/" + MonthCode(sdate.month) + "/fo" + DayCode(sdate.day) + MonthCode(sdate.month) + str(sdate.year) + "bhav.csv.zip"
    url = site + path
    if exists(url) == False:
        sdate += delta
        continue
    print (url)
    req = requests.get(url)
    fileName = home + str(sdate.year) + "\\" + MonthCode(sdate.month) + "-" + str(sdate.year) + "\\" + str(sdate.day) + "-" + str(sdate.month) + "-" + str(sdate.year) + ".zip"
    directory(fileName)
    file = open(fileName, 'wb')
    for chunk in req.iter_content(100000):
        file.write(chunk)
    file.close()
    sdate += delta
