import requests
import os


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

for year in range(2016, 2016 + 1):
    for month in range(1, 2):
        for day in range(15, FindDays(month, year) + 1):
            path = "/content/historical/DERIVATIVES/" + str(year) + "/" + MonthCode(month) + "/fo" + DayCode(day) + MonthCode(month) + str(year) + "bhav.csv.zip"
            url = site + path
            if exists(url) == False:
                continue
            print (url)
            req = requests.get(url)
            fileName = home + str(year) + "\\" + MonthCode(month) + "-" + str(year) + "\\" + str(day) + "-" + str(month) + "-" + str(year) + ".zip"
            directory(fileName)
            file = open(fileName, 'wb')
            for chunk in req.iter_content(100000):
                file.write(chunk)
            file.close()
