import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import threading
import time
browser = webdriver.Firefox()
browser.get('http://192.168.1.92/Logon')
uname = browser.find_element_by_name("Username")
uname.clear()
uname.send_keys("vipin")
pwd = browser.find_element_by_name("Password")
pwd.clear()
pwd.send_keys("seeroo1988")
pwd.send_keys(Keys.RETURN)
def is_text_present(text):
    try:
        browser.find_element_by_xpath(text) # find body tag element
    except NoSuchElementException:
        return False
    return True
if is_text_present('//button[contains(.,"Close")]'):
    browser.find_element_by_xpath('//button[contains(.,"Close")]').click()
browser.find_element_by_xpath('//a[img/@src="/Images/Timesheet.png"]').click()
browser.find_element_by_link_text('Add Timesheet').click()

def multiselect_set_selections(driver, element_id, labels):
    el = driver.find_element_by_id(element_id)
    for option in el.find_elements_by_tag_name('option'):
        if option.text in labels:
            option.click()



for file in os.listdir("D:\\seeroo_timesheet\\"):
    #time.sleep(2)
    if file.endswith(".txt"):        
        fo = open("D:\\seeroo_timesheet\\"+str(file), "r")
        line = fo.readline()        
        first_two_digits = line[:2]
        intime=line[12:20]
        print("intime"+intime)
        print(first_two_digits)
        browser.implicitly_wait(3)
        browser.find_element_by_xpath("//input[@name='TodayDatePicker']").click()
        browser.implicitly_wait(3)
        browser.find_element_by_xpath("//button[contains(.,'Yes')]").click()
        browser.implicitly_wait(8)
        browser.find_element_by_xpath("//a[contains(.,'"+first_two_digits+"')]").click()
        fo.seek(0)
        lineList = fo.readlines()
        outtime=lineList[-1][0:8]
        print("outtime"+outtime)
        inT = browser.find_element_by_name("InTime")
        inT.clear()
        inT.send_keys(intime)
        outT = browser.find_element_by_name("OutTime")
        outT.clear()
        outT.send_keys(outtime)
        browser.implicitly_wait(3)
        multiselect_set_selections(browser,"ProjectId","ETH -JAVA")
        browser.implicitly_wait(3)
        multiselect_set_selections(browser,"CategoryId","Development")
        for item in lineList[1:len(lineList)]:
            print (item)
            lineSplit=item.strip().split("$$")
            txtTsk=browser.find_element_by_id("txtTask")
            txtTsk.clear()
            txtTsk.send_keys(lineSplit[1])
            browser.implicitly_wait(3)
            multiselect_set_selections(browser,"Status","Completed")
            browser.implicitly_wait(3)
            txtWorkingHours=browser.find_element_by_id("txtWorkingHours")
            txtWorkingHours.clear()
            txtWorkingHours.send_keys(lineSplit[2])            
            browser.implicitly_wait(3)
            browser.find_element_by_id("btnsubmit").click()
            browser.implicitly_wait(15)
        browser.find_element_by_xpath("//input[contains(@value,'Submit')]").click()
        alert = browser.switch_to_alert()
        alert.accept()
