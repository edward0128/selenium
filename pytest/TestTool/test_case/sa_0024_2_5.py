import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0024_2_5_goto(self):  
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button") == True
    return True





