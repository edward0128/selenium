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
    
  def SA_0028(self):
    connect_web(self)
    login_web(self,self.vars["account_user"][0],self.vars["account_password"][0])
    click_button(self,By.XPATH,"//li[4]/span/span","Projects","Click project button")
    #  username=(get_text(self,By.XPATH,"//tr[2]/td[2]/span","get User Management "))
    count=0
    for i in range(2, 50, 1):
        try:
          current_project=get_text(self,By.XPATH,"//tr[%d]/td[2]/span" % (i),"search project_name")
          ini_project=self.vars["project_name"] #導入data-base的project name
          project＿naeme_path = "//tr[%d]/td[2]/span" % (i)

          if current_project == "":
            logging.info("Not find the correspond project name or process is end")
            break
          if current_project =="admin":
            logging.info("Not find the correspond project name")
            break
          
          for project in ini_project:
            if project == current_project:
              click_button(self,By.XPATH,project＿naeme_path,project,"Click project name %s"% (project))
              click_button(self,By.XPATH,"//button[2]/span/span/span","Solution","Click the solution item %s"%(project))
              time.sleep(1)
              count=count+1
              for i in range(1, 10, 1):
                  #slide_button是bar的按鈕，solution_select也是bar的按鈕，只是路徑表達的方式不同
                slide_button="return document.evaluate('//tr[%d]//td[7]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" %(i)
                solution_selcet="//tr[%d]/td[7]/span/span/span/input" %(i)
                date_s="//tr[%d]/td[6]/span" %(i)
                user1=(get_text(self,By.XPATH,date_s,"get date path ")) #以日期作為判斷依據，若空白就跳出
            # slide_button="return document.evaluate('//tr[1]//td[7]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" 
            # solution_selcet="//tr[1]/td[7]/span/span/span/input" 
            # slide_button1="return document.evaluate('//tr[3]//td[7]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" 

              # print(project)
              # print(user1)
              
                if user1=="":
                  break
                else :
                  enble_project_solution(self,slide_button,solution_selcet)                
            
              click_button(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/i[2]","","click")  
 
              ###count 還沒處理
              # click_button(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[1]/i[2]","","click")  
              # time.sleep(5)

        except:
          logging.error("user not found")

     

 
    #click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button")
    #check_text(self,By.XPATH,"//span[contains(.,'Log In')]","Log In","check login page")
    time.sleep(5)
    
if __name__ == "__main__":
  driver = SeleniumTest()
  driver.setup_method()
  driver.SA_0028()
  driver.teardown_method()