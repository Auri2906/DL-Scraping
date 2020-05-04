from selenium import webdriver  
import time  
from selenium.webdriver.common.keys import Keys
import requests
import json
from lxml import html
import urllib.request

print("Application Started..........\n Warning : plz minimize chrome and only open it while seeing captcha")  
driver = webdriver.Chrome("C:\\Users\\DELL\\Desktop\\chromedriver_win32\\chromedriver.exe") 
 
  
 
driver.get("https://parivahan.gov.in/rcdlstatus/?pur_cd=101")

str = input("Enter Driving License No.: ")
driver.find_element_by_name("form_rcdl:tf_dlNO").send_keys(str)  
time.sleep(1)  

str = input("Enter DOB: ")
driver.find_element_by_name("form_rcdl:tf_dob_input").send_keys(str)  
time.sleep(1)  

str = input("Enter CaptchaID : ")
driver.find_element_by_name("form_rcdl:j_idt34:CaptchaID").send_keys(str)  
time.sleep(1)  


driver.find_element_by_name("form_rcdl:j_idt46").send_keys(Keys.ENTER)  
time.sleep(1)


status = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[1]/td[2]/span').text
name = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[2]/td[2]').text
doi = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[3]/td[2]').text
last_trans = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[1]/tbody/tr[4]/td[2]').text
doe = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt118"]/table[2]/tbody/tr[1]/td[3]').text
category = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[1]').text
cov = driver.find_element_by_xpath('//*[@id="form_rcdl:j_idt167_data"]/tr/td[2]').text

data = {
    "status" : status,
    "holder name" : name,
    "date of issue" : doi,
    "date of expiry" : doe,
    "last transaction at" : last_trans,
    "category" : category,
    "vehicle class" : cov
}

data = json.dumps(data)
print(data)
