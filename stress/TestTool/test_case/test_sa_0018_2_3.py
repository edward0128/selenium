import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def test_sa_0018_2_3_check(self):
    assert connect_web(self,"test-sa-0018") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True

    assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True
    
    assert check_text(self,By.XPATH,"//li[3]/div/span/span","Users","check Users") == True
    assert click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users") == True
    
    assert check_text(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check Users") == True
    assert check_text(self,By.XPATH,"//li[3]/ul/li[2]/span/span","User Activation","check Users") == True
    
    assert click_button(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"click admin button") == True
    assert click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button") == True
    assert check_text(self,By.XPATH,"//span[contains(.,'Log In')]","Log In","check login page") == True