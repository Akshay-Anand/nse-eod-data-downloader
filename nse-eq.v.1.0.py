import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
i=int(input("Enter the no. of companies:"))
while(i>0):
    company = input("Enter Company Symbol Here:")
    dr=int(input("Choose your date range by entering the number alongside your choice:\n1 for 1 day\n2 for 1 month\n3 for 3 month\n4 for 1 year\n5 for 2 years\n"))
    if (dr == 1):
        dat="day"
    elif (dr == 2):
        dat="1month"
    elif (dr==3):
        dat="3month"
    elif (dr==4):
        dat="12month"
    elif (dr==5):
        dat="24month"
    else:
        print("ERROR:Please check the number entered")
        break
    driver = webdriver.Firefox()
    driver.get("https://www.nseindia.com/products/content/equities/equities/eq_security.htm")
    sym = driver.find_element_by_id("symbol")
    sym.send_keys(company)
    date = Select(driver.find_element_by_id("dateRange"))
    date.select_by_value(dat)
    driver.find_element_by_class_name("getdata-button").click()
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('download-data-link').click()
    i=i-1
    

