import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def test_sa_0018_2_3_1_goto(self):
    assert connect_web(self,"test-sa-0019") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    # Check login  
    assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True
  
    assert check_text(self,By.XPATH,"//li[3]/div/span/span","Users","check Users") == True
    assert click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users") == True
    
    assert check_text(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == True
    assert click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == True

def test_sa_0018_2_3_1_create_user(self):
    for val in self.vars["account_user"]:
        if val == "admin":
          continue
        assert create_user(self,val,val) == True

    time.sleep(3)
    # try:
    #   logging.info("scroll to mid")
    #   scroll_down="document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scroll(0,%s)" % ("10000")
    #   get_scroll_height="return document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scrollTop"
    #   self.driver.execute_script(scroll_down)
    #   scroll_height=int(self.driver.execute_script(get_scroll_height))
    #   scroll_down_mid="return document.evaluate('/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.scroll(0,%s)" % (scroll_height/2)
    #   self.driver.execute_script(scroll_down_mid)
    # except:
    #   logging.error("scroll error")

def test_sa_0018_2_3_1_check(self):
    account_user_dict = {}
    for i in range(1, 50, 1):
      user_target = "//tr[%d]/td[3]/span" % (i)
      username=(get_text(self,By.XPATH,user_target,"get User Management "))
      
      email_target = "//tr[%d]/td[4]/span" % (i)
      email=(get_text(self,By.XPATH,email_target,"get User Management "))
      
      logging.info('get user name = %s',username)
      logging.info('get user email = %s',email)
      if username=="":
        break
      account_user_dict[username]=email

    count=0
    for host in self.vars["account_user"]:
        assert host in account_user_dict
        assert account_user_dict[host] == self.vars["account_user"][count]+"@geminiopencloud.com"
        count=count+1