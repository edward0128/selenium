import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0025_2_5_1_goto(self):  
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button") == True
    return True

def sa_0025_2_5_1_create_project(self): 
    count=0
    for project in self.vars["project_name"]:
      status=create_project(self,project,self.vars["project_quota_cpu"][count],self.vars["project_quota_mem"][count],self.vars["project_quota_gpu"][count],self.vars["project_description"][count])
      if status == False:
        logging.error("Create project error. Project = %s",project)
        return False
      self.driver.refresh()
      count+=1
    logging.info("Create project success")
    return True

