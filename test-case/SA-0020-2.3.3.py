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
    
  def SA_0018(self):
##############enable user and check ####################
    connect_web(self)
    login_web(self,self.vars["account_user"][0],self.vars["account_password"][0])
    
    logging.info("###go to the User Management###")
    check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login")
    check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login")   
    check_text(self,By.XPATH,"//li[3]/div/span/span","Users","check Users")
    click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users")
    check_text(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management")
    click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management")
    time.sleep(3)

    logging.info("###scroll to mid###")
    try:
      logging.info("scroll to mid")
      scroll_down="document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scroll(0,%s)" % ("10000")
      get_scroll_height="return document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollTop"
      self.driver.execute_script(scroll_down)
      scroll_height=int(self.driver.execute_script(get_scroll_height))
      scroll_down_mid="return document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scroll(0,%s)" % (scroll_height/2)
      self.driver.execute_script(scroll_down_mid)
    except:
      logging.error("scroll error")
    
    logging.info("###disable all user###")
    logging.info("Start to enable user")
    for host in self.vars["account_user"]:
      if host == "admin":
          continue
      if disable_user(self,host) == False :
          logging.error("User can't Disable %s",host)
          self.driver.quit()

    logging.info("###logout###")
    click_button(self,By.XPATH,"//div[4]/button/span/span[2]","admin","click admin button")
    click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button")

    logging.info("###check user login (all user can't login)###")
    count=0
    for var in self.vars["account_user"]:
      self.driver.find_element(By.NAME, "email").clear()
      self.driver.find_element(By.NAME, "password").clear()
      if test_login_web(self,var,self.vars["account_password"][count]) == False:
        logging.info("User = %s PASS (User dissable)",var)
      else:
        if var == "admin":
          continue
        logging.error("User = %s ERROR (User not dissable)",var)
        self.driver.quit()
      count+=1
      self.driver.refresh()


##############dissable user and check ####################
    login_web(self,self.vars["account_user"][0],self.vars["account_password"][0])
    time.sleep(3)
    logging.info("###go to the User Management###")
    check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login")
    check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login")   
    
    logging.info("###go to the User Management###")
    if check_text(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == "":
      check_text(self,By.XPATH,"//li[3]/div/span/span","Users","check Users")
      click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users")
    check_text(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management")
    click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management")
    time.sleep(3)

    logging.info("###disable all user###")
    for host in self.vars["account_user"]:
      if host == "admin":
        continue
      if enable_user(self,host)==False:
        logging.error("User can't enable_user %s",host)
        self.driver.quit()
    time.sleep(5)

    logging.info("###logout###")
    click_button(self,By.XPATH,"//div[4]/button/span/span[2]","admin","click admin button")
    click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button")

    logging.info("###check user login###")
    count=0
    for var in self.vars["account_user"]:
      self.driver.find_element(By.NAME, "email").clear()
      self.driver.find_element(By.NAME, "password").clear()
      if test_login_web(self,var,self.vars["account_password"][count]) == False:
        if var == "admin":
          continue
        logging.error("User = %s ERROR (User can't login)",var)
        self.driver.quit()
      else:
        logging.info("User = %s PASS (User login success)",var)
      count+=1
      self.driver.refresh()



if __name__ == "__main__":
  driver = SeleniumTest()
  driver.setup_method()
  driver.SA_0018()
  driver.teardown_method()
