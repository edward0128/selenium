# Generated by Selenium IDE
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
from TestTool.test_case.sa_test import*
class TestDemotest():
  def setup_method(self, method):

    self.vars={}
    init_log("/Users/yu-sung/Documents/ci/gmn-1.0.46-autotesting/selenium/test-case/selenium.log",logging.INFO)
    start_test(os.path.basename(__file__))
    read_config(self,"../config.ini")
    try:
      self.driver = init_driver(self)
      self.driver.implicitly_wait(10)
    except:
      logging.error('Prepare webdriver error', exc_info=True)

  def teardown_method(self):
    self.driver.quit()

  def test_sa_0001_1_1(self):
    sa_0001_1_1_check(self)

  def test_sa_0002_1_2(self):
    sa_0002_1_2_check(self)

  def test_sa_0003_2_1(self):
    sa_0003_2_1_goto(self)
    sa_0003_2_1_check(self)
  
  def test_sa_0004_2_2(self):
    sa_0004_2_2_goto(self)
    sa_0004_2_2_check(self)
    time.sleep(int(self.vars["DelayTime"]))
  
  def test_sa_0018_2_3(self):
    sa_0018_2_3_check(self)

  def test_sa_0019_2_3_1(self):
    sa_0018_2_3_1_goto(self)
    sa_0018_2_3_1_create_user(self)
    sa_0018_2_3_1_check(self)
  
  def test_sa_0020_2_3_3(self):
    logging.info("Start to connect web")
    assert connect_web(self,"test-sa-0020") == True

    logging.info("Start to go to user page")
    assert sa_0020_2_3_3_goto(self) == True

    logging.info("Start to disable all user.")
    assert sa_0020_2_3_3_disable(self) == True
    
    logging.info("Start to logout.")
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[4]/button/span[1]/span[2]","admin","click admin button") == True
    assert click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button") == True

    logging.info("Start to check disable login.")
    assert sa_0020_2_3_3_check_notlogin(self) == True

    logging.info("Start to check disable login.")
    assert sa_0020_2_3_3_goto(self) == True

    logging.info("Start to enable all user.")
    assert sa_0020_2_3_3_enable(self) == True

    logging.info("Start to logout.")
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[1]/div[4]/button/span[1]/span[2]","admin","click admin button") == True
    assert click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button") == True
    assert sa_0020_2_3_3_check_login(self) == True

  def test_sa_0021_2_3_2(self):
    assert connect_web(self,"test-sa-0021") == True
    logging.info("Start to go to user management.")
    assert sa_0021_2_3_2_goto(self) == True
    logging.info("Try to delete user")
    assert sa_0021_2_3_2_delete(self)== True
    logging.info("Check delete user")
    assert sa_0021_2_3_2_check(self) == True

  def test_sa_0024_2_5(self):
    assert connect_web(self,"test_sa_0024_2_5") == True
    assert sa_0024_2_5_goto(self) == True
  def test_sa_0025_2_5_1(self):
    assert connect_web(self,"test_sa_0025_2_5_1") == True  
    assert sa_0024_2_5_goto(self) == True
    assert sa_0025_2_5_1_create_project(self) == True
  def test_sa_0026_2_5_3(self):
    assert connect_web(self,"test_sa_0026_2_5_3") == True 
    assert sa_0024_2_5_goto(self) == True
    assert sa_0026_2_5_3_check_description(self) == True
  def test_sa_0027_2_5_2(self):
    assert connect_web(self,"test_sa_0027_2_5_2") == True
    assert sa_0024_2_5_goto(self) == True
    assert sa_0027_2_5_2_delete_project(self) == True
    assert sa_0027_2_5_2_check_project(self) == True
  def test_sa_0028_2_5_4(self):
    sa_0028_2_5_4_goto(self)
    sa_0028_2_5_4_enable_solution(self)
  def test_sa_0030_2_5_6(self):
    assert connect_web(self,"test_sa_0030_2_5_6") == True
    
  def test_sa_0035_2_6_1(self):
    assert connect_web(self,"test_sa_0035_2_6_1") == True
  def test_sa_0036_2_6_2(self):
    assert connect_web(self,"test_sa_0036_2_6_2") == True



