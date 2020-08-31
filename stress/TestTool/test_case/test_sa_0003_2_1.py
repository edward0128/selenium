import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def test_sa_0003_2_1_goto(self):
    assert connect_web(self,"test-sa-0003") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert check_text(self,By.XPATH,"//li/span/span","Modules","check module") == True
    logging.info('Change to the module page')
    assert click_button(self,By.XPATH,"//li/span/span","Modules","click module button") == True
    logging.info('Get all of the module item')

def test_sa_0003_2_1_check(self):
    module_dict = {}
    for i in range(1, 6, 1):
      module_key=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span"% (str(i),1),"get module_key")
      module_value=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span"% (str(i),2),"get module_value")
      logging.info('Find Modules %s = %s',module_key,module_value)
      module_dict[module_key]=module_value
    assert "k8s-container" in module_dict
    assert "k8s-job" in module_dict
    time.sleep(int(self.vars["DelayTime"]))