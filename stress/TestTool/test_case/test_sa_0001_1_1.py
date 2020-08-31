import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def test_sa_0001_1_1_check(self):
    assert connect_web(self,"test-sa-0001") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True