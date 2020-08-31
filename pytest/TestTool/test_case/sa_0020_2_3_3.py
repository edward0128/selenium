import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0020_2_3_3_goto(self):
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") ==True
    assert check_text(self,By.XPATH,"//li[3]/div/span/span","Users","check Users") == True
    
    ### User Management not found need to click button
    if get_text(self,By.XPATH,"//li[3]/ul/li/span/span","Get User Management") == "":
        assert click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users") == True

    assert click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == True

    time.sleep(1)
    return True

def sa_0020_2_3_3_disable(self):
    for host in self.vars["account_user"]:
       if host == "admin":
           continue
       assert disable_user(self,host) == True
    return True
def sa_0020_2_3_3_enable(self):
    for host in self.vars["account_user"]:
      if host == "admin":
        continue
      if enable_user(self,host)==False:
        logging.error("Can't enable_user %s",host)
        return False
    return True


def sa_0020_2_3_3_check_notlogin(self):
    count=0
    for host_name in self.vars["account_user"]:
      self.driver.find_element(By.NAME, "email").clear()
      self.driver.find_element(By.NAME, "password").clear()

      if host_name == "admin":
        continue
      assert try_login_web(self,host_name,self.vars["account_password"][count]) == False
      count=count+1
    self.driver.find_element(By.NAME, "email").clear()
    self.driver.find_element(By.NAME, "password").clear()
    return True

def sa_0020_2_3_3_check_login(self):
    count=0
    for host_name in self.vars["account_user"]:
      self.driver.find_element(By.NAME, "email").clear()
      self.driver.find_element(By.NAME, "password").clear()

      if host_name == "admin":
        continue
      assert try_login_web(self,host_name,self.vars["account_password"][count]) == True
      count=count+1
    self.driver.find_element(By.NAME, "email").clear()
    self.driver.find_element(By.NAME, "password").clear()
    return True