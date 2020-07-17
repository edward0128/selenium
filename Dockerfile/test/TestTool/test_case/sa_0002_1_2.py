import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0002_1_2_check(self):
    assert connect_web(self,"test-sa-0002") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    # Check login  
    assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True
    # click admin button
    assert click_button(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"click admin button") == True
    # click logout button
    assert click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button") == True
    # Detect login page
    assert check_text(self,By.XPATH,"//span[contains(.,'Log In')]","Log In","check login page") == True