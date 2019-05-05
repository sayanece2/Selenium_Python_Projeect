# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 11:57:30 2019

@author: 007
"""
import FunctionLibrary as fl
#from selenium import webdriver

print("Test Case 1:")
ResPath=fl.setup("TC1")
url="http://www.facebook.com"
driver=fl.open_url("1",url,ResPath)
fl.click(driver,"2","//*[@id='u_0_11']",ResPath)
fl.validateText(driver,"3","Create an accout","//*[@id='content']/div/div/div/div/div[2]/div[1]/div[1]/span",ResPath)

#driver.get("http://www.facebook.com")

