import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *
from TestTool.init import *


class TestDemotest():
  def setup_method(self, method):
    
    self.vars={}
    init_log("/Users/yu-sung/Documents/ci/gmn-1.0.46-autotesting/selenium/test-case/selenium.log",logging.INFO)
    start_test(os.path.basename(__file__))
    read_config(self,"../config.ini")
    try:
      self.driver = init_driver(self)
    except:
      logging.error('Prepare webdriver error', exc_info=True)
      self.driver.quit()
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_demotest2(self):
    print("start to test")
    value=4
    assert value==4
    connect_web(self)
    login_web(self,self.vars["account_user"][0],self.vars["account_password"][0])

