# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:12:40 2019

@author: 007
"""

import os
import unittest
from appium import webdriver
from time import sleep
 
class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"
    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        #desired_caps['platformVersion'] = '8.0'
        desired_caps['deviceName'] = 'My Phone'
        desired_caps['noReset'] = 'true'
        # Returns abs path relative to this file and not cwd
        #desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__),'apps/Chess Free.apk'))
        desired_caps['appPackage'] = 'arjuntoshniwal.androidtutorials.advanced'
        desired_caps['appActivity'] = 'arjuntoshniwal.androidtutorials.advanced.SwipeActivity'
        self.driver = webdriver.Remote('http://192.168.181.2:4723/wd/hub', desired_caps)
 
    def tearDown(self):
        "Tear down the test"
        self.driver.quit()
 
    def test_single_player_mode(self):
        "Test the Chess app launches correctly and click on Play button"
        element = self.driver.find_element_by_xpath("//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.a.c[2]/android.widget.TextView")
        element.click()
        sleep(5)
 
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)