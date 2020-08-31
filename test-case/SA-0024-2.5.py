# Generated by Selenium IDE
import pytest
import time
import json
import logging
import os
import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from TestTool.init import *
from TestTool.control import *
from TestTool.task import *
class SeleniumTest():
  def setup_method(self):
    init_log("selenium.log",logging.INFO)
    start_test(os.path.basename(__file__))
    self.vars={}
    read_config(self,"../config.ini")

    try:
      self.driver = init_driver(self)
    except:
      logging.error('Prepare webdriver error', exc_info=True)
      self.driver.quit()
  
  def teardown_method(self):
    end_test(os.path.basename(__file__))
    self.driver.quit()
    
  def SA_0022(self):
    connect_web(self)
    login_web(self,self.vars["account_user"][0],self.vars["account_password"][0])
    click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button")
    click_button(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"click admin button")
    click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button")
    check_text(self,By.XPATH,"//span[contains(.,'Log In')]","Log In","check login page")
    time.sleep(2)
    
if __name__ == "__main__":
  driver = SeleniumTest()
  driver.setup_method()
  driver.SA_0022()
  driver.teardown_method()