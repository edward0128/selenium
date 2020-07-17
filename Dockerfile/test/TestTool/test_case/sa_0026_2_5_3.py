import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0026_2_5_3_goto(self):  
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button") == True
    return True

def sa_0026_2_5_3_check_description(self):  
    dict_checkstatus={}
    for i in range(1, 50, 1):
      user_target = "//tr[%d]/td[2]/span" % (i)
      username=(get_text(self,By.XPATH,user_target,"Get project name"))
      if username =="":
        break
      count=0
      for project in self.vars["project_name"]:
        if username==project:
          assert click_button(self,By.XPATH,"//a[contains(.,'%s')]" % (username),username,"Click project %s" % username) == True
          if get_text(self,By.XPATH,"//td[contains(text(),'%s')]"%(username),"Get project description %s" % username )!=username:
            logging.error("Porject %s name error",username)
            break
          else:
            logging.info("Project %s name success" % username)
          
          if get_text(self,By.XPATH,"//td[contains(text(),'%s')]"%(self.vars["project_description"][count]),"Get project description %s" % self.vars["project_description"][count] )!=self.vars["project_description"][count]:
            logging.error("Porject %s description error",self.vars["project_description"][count])
            break
          else:
            logging.info("Project %s description success " % self.vars["project_description"][count])
          assert click_button(self,By.XPATH,"//div/div/i[2]","","Close project detail %s" % username) == True
          logging.info("Project check %s success",username)
          dict_checkstatus[username]="checked"
        count+=1

    for project in self.vars["project_name"]:

      if project in dict_checkstatus:
        logging.info("Check project success. Project =  %s",project)
      else:
        logging.error("Can't get project description %s",project)
        return False
    
    logging.info("Check project success")
    return True


