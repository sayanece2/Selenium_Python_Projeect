# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:54:26 2019

@author: 007
"""
import os
from selenium import webdriver
import datetime


#Initializing driver
driver = webdriver

def open_url(step,url,TcPath):
    driver=webdriver.Chrome()
    driver.maximize_window()
    method_name="open_url"
    try:
        driver.get(url)
        print("Step:",step," ",method_name," :: executed successfully -- PASS")
        log=open(TcPath+"\\"+"log.txt", "a")
        log.write("Step:"+step+" "+method_name+" :: executed successfully -- PASS")
        log.write("\n")
        log.close()
        return driver
    except:
        print("Step:",step," ",method_name,":: could not be executed -- FAIL")
        log=open(TcPath+"\\"+"log.txt", "a")
        log.write("Step:",step," ",method_name,":: could not be executed -- FAIL")
        log.write("\n")
        log.close()
        
    
def click(driver,step,xpath,TcPath):
    method_name="click"
    try:
        driver.find_element_by_xpath(xpath).click()
        print("Step:",step," ",method_name," :: executed successfully -- PASS")
        log=open(TcPath+"\\"+"log.txt", "a")
        log.write("Step:"+step+" "+method_name+" :: executed successfully -- PASS")
        log.write("\n")
        log.close()
        
    except:
        print("Step:",step," ",method_name,":: could not be executed -- FAIL")
        log=open(TcPath+"\\"+"log.txt", "a")
        log.write("Step:"+step+" "+method_name+":: could not be executed -- FAIL")
        log.write("\n")
        log.close()

def setup(tcName):
    cwd = os.getcwd()
    print("Current dir::",cwd)
    currentDT = datetime.datetime.now()
    currentDT=(currentDT.strftime("%Y-%m-%d_%H-%M-%S"))
    path=cwd+"\\Result\\"+"Exe_"+str(currentDT)
    TcPath=path+"\\"+tcName
    try:
        os.mkdir(path)
        os.mkdir(TcPath)
        print("Result Directory created")
        print("Set Up done")
        log=open(TcPath+"\\"+"log.txt", "a")
        log.close()
        return TcPath
    except:
        print("Could not create directory")
    
    
def validateText(driver,step,expTxt,xpath,ResPath):
    method_name="validateText"
    try:
        actualTxt=driver.find_element_by_xpath(xpath).text
        if actualTxt==expTxt:
            print("Expected and Actual text are same")
            print("Step:",step," ",method_name," :: executed successfully -- PASS")
            log=open(ResPath+"\\"+"log.txt", "a")
            log.write("Step:"+step+" "+method_name+" :: executed successfully -- PASS")
            log.write("\n")
            log.close()
        else:
            driver.save_screenshot(ResPath+"\\"+"Step"+step+".png")
            print("Expected and Actual text are not same")
            print("Step:",step," ",method_name,":: could not be executed -- FAIL")
            log=open(ResPath+"\\"+"log.txt", "a")
            log.write("Step:"+step+" "+method_name+":: could not be executed -- FAIL")
            log.write("\n")
            log.close()
    
    except:
        print("Step:",step," ",method_name,":: could not be executed -- FAIL")
        log=open(ResPath+"\\"+"log.txt", "a")
        log.write("Step:"+step+" "+method_name+":: could not be executed -- FAIL")
        log.write("\n")
        log.close()
            
    
    