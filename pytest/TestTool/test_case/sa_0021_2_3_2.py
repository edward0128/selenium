import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0021_2_3_2_goto(self):  
  assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
  assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True
  assert click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users") == True
  assert click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == True
  return True
def sa_0021_2_3_2_delete(self):
  select_success=False
  for host in self.vars["account_user"]:
    select_success=delete_user(self,host)

  if select_success == False:
    logging.warning("User not select and not delete.")
  
  if select_success == True:
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[2]/button[3]/span[1]/i","","Click Delete user buton") == True
    assert click_button(self,By.XPATH,"/html/body/div[3]/div[2]/div[3]/button[2]/span[1]","Confirm","Confirm Delete user") == True
    
  return True
def sa_0021_2_3_2_check(self):
  
  dict_user={}
  for i in range(2, 50, 1):
    
    user_target = "//tr[%d]/td[3]/span/a" % (i)
    username=get_text(self,By.XPATH,user_target,"get User Management ")
    
    if username == "":
      break
    if username == "admin":
      continue
    dict_user[username]="select"
  
  for host in self.vars["account_user"]:
    if host == "admin":
      continue
    if host in dict_user:
      logging.error("Can't delete user. User = %s",host)
      return False
    else:
       logging.info("Check User= %s and User %s is deleted.",host,host)     

  return True


