import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0028_2_5_4_goto(self):  
    assert connect_web(self,"test_sa_0028_2_5_24") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button") == True

def sa_0028_2_5_4_enable_solution(self):
    for i in range(2, 50, 1):
      current_project=get_text(self,By.XPATH,"//tr[%d]/td[2]/span" % (i),"search project_name")
      ini_project=self.vars["project_name"]
      project＿naeme_path = "//tr[%d]/td[2]/span" % (i)

      if current_project == "":
        logging.info("Not find the correspond project name or process is end")
        break
      if current_project =="admin":
        logging.info("Not find the correspond project name")
        break
      
      for project in ini_project:
        if project == current_project:
          assert click_button(self,By.XPATH,project＿naeme_path,project,"Click project name %s"% (project)) == True
          assert click_button(self,By.XPATH,"//button[2]/span/span/span","Solution","Click the solution item %s"%(project)) == True
          time.sleep(1)
          for i in range(1, 10, 1):
            slide_button="return document.evaluate('//tr[%d]//td[7]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" %(i)
            solution_selcet="//tr[%d]/td[7]/span/span/span/input" %(i)
            solution_name="/html/body/div[1]/div/div[1]/div[2]/div/div[3]/div/div[2]/div/div[3]/div/div[2]/div/div/div[2]/table/tbody/tr[%d]/td[1]/span" %(i)
            solution_name=get_text(self,By.XPATH,solution_name,"")
            if solution_name=="":
              break
            else :
              if solution_name in self.vars["solution"]:
                assert enble_project_solution(self,slide_button,solution_selcet) == True
          assert click_button(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/i[2]","","Close solutions") == True
    return True
