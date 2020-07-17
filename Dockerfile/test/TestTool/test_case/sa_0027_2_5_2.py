import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0027_2_5_2_goto(self):  
  assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
  assert check_text(self,By.XPATH,"//div[4]/button/span/span[2]",self.vars["account_user"][0],"check login") == True
  assert click_button(self,By.XPATH,"//li[3]/div/span/span","Users","click Users") == True
  assert click_button(self,By.XPATH,"//li[3]/ul/li/span/span","User Management","check User Management") == True
  return True

def sa_0027_2_5_2_delete_project(self):
    delete_status=False
    for project in self.vars["project_name"]:
      if delete_project(self,project) == True:
        delete_status = True
    
    if delete_status == True:
      click_button(self,By.XPATH,"//button/span/i","","Delete project")
      time.sleep(3)
      self.driver.refresh()
      time.sleep(5)
    
    if delete_status == False:
      logging.warning("Can't not delete any project")

    return True

def sa_0027_2_5_2_check_project(self):

    project_dict={}
    for i in range(1, 50, 1):
      project_target = "//tr[%d]/td[2]/span" % (i)
      project_name=(get_text(self,By.XPATH,project_target,"Get project name"))
      if project_name =="":
        break
      logging.info("Get project name  = %s",project_name)
      project_dict[project_name]=project_name

    for project in self.vars["project_name"]:
      if project in project_dict:
        logging.error("Project can't delete project = %s",project)
        return False
    return True

