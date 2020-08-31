import logging
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from TestTool.control import *

def create_user(self,username,usermail):
    click_button(self,By.XPATH,"//span[contains(.,'Add User')]","Add User","Click Add User")
    
    set_text(self,By.XPATH,"//input[@name='name']",username,"set user name")
 
    set_text(self,By.XPATH,"//input[@name='email']",usermail+"@gmail.com","set user email")
    
    click_button(self,By.XPATH,"//span[contains(.,'Submit')]","Submit","Click Submit")
    time.sleep(3)
    
    result = get_text(self,By.XPATH,"//span/div/div/div/div[2]","get submit email")


    if result =="\"User Create success but send invited mail fail with error: get smtp client error NO SMTP SETTING IN DB.Please Check smtp setting\"":
      logging.warning("smtp server not setting create username=%s",username)
    elif result == "\"ACCOUNT ALREADY EXIST\"":
      logging.warning("ACCOUNT ALREADY EXIST create username=%s",username)
    else:
      logging.info("Create user finish create username=%s",username)
    
    self.driver.refresh()

def delete_user(self,host):
      try:
          for i in range(2, 50, 1):
            user_target = "//tr[%d]/td[3]/span/a" % (i)
            username=(get_text(self,By.XPATH,user_target,"get User Management "))
            user_select = "//tr[%d]/td[1]/span" % (i)
            
            if username =="":
              break
            if host == "admin":
              break
            if username == host:
              click_button(self,By.XPATH,user_select,"","user select")
              return True
          return False
      except:
        logging.error('user not found = %s',host)
        self.driver.quit()

def enable_user(self,host):
      try:
          for i in range(2, 50, 1):
            user_target = "//tr[%d]/td[3]/span/a" % (i)
            username=(get_text(self,By.XPATH,user_target,"get User Management "))
            user_select = "//tr[%d]/td[7]/span" % (i)

            if username =="":
              break
            if host == "admin":
              break
            if username == host:
              slide_button= "return document.evaluate('//tr[%d]//td[7]//span[1]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" % (i)
              logging.info("slide_button = %s",slide_button)
              if (self.driver.execute_script(slide_button)) < 37:
                click_button(self,By.XPATH,user_select,"","user select")
              return True
          return False
      except:
        logging.error('user not found = %s',host)
        self.driver.quit()

def disable_user(self,host):
      try:
          for i in range(2, 50, 1):
            user_target = "//tr[%d]/td[3]/span/a" % (i)
            username=(get_text(self,By.XPATH,user_target,"get User Management "))
            user_select = "//tr[%d]/td[7]/span" % (i)

            if username =="":
              break
            if host == "admin":
              break
            if username == host:
              slide_button= "return document.evaluate('//tr[%d]//td[7]//span[1]//span[1]//span[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length" % (i)
              logging.info("slide_button = %s",slide_button)
              if int(self.driver.execute_script(slide_button)) >= 37:
                click_button(self,By.XPATH,user_select,"","user select")
              return True
          return False
      except:
        logging.error('user not found = %s',host)
        self.driver.quit()


def create_flavor(self,i):
      try:
          click_button(self,By.XPATH,"//span[contains(text(),'Create Flavor')]","Create Flavor","click Create Flavors button,")
          logging.info("---------create flavor-------")
          click_button(self,By.XPATH,"//div[@id='root']/div/div[2]/div[2]/div[2]/div/div/div/div/div/div","","click platform button,")
          click_button(self,By.XPATH,"//div[@id='menu-platformName']/div[2]/ul/li","default_k8s","click default_k8s")
          time.sleep(0.5)
          set_text(self,By.XPATH,"//input[@name='flavorName']",self.vars["flavor_name"][i],"input flavor name")
          set_text(self,By.XPATH,"//input[@name='cpu']",self.vars["flavor_cpu"][i],"input cpu quota")
          set_text(self,By.XPATH,"//input[@name='memory']",self.vars["flavor_memory"][i],"input memory quota")
          set_text(self,By.XPATH,"//input[@name='disk']",self.vars["flavor_disk"][i],"input disk quota")
          set_text(self,By.XPATH,"//input[@name='gpu']",self.vars["flavor_gpu"][i],"input gpu quota")
          click_button(self,By.XPATH,"//span[contains(.,'Submit')]","Submit","submit,")
          logging.info("---------submit-------")
          time.sleep(4)
          result = get_text(self,By.XPATH,"//span/div/div/div/div[2]","get Error message")
          print(result)
          if "already exists on default_k8s" in result:
              logging.warning("flavor name ALREADY EXIST create")
          else :
              logging.info("Create user finish create flavor_name=%s",self.vars["flavor_name"][i])
          self.driver.refresh()  
      except :
        logging.error("Can't create flavor")
        self.driver.quit()

def delete_flavor(self):
      count=0
      try:
          for i in range(2, 50, 1):
            flavor_key=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span/a"% (str(i),2),"search flavor_key")
            flavor_value=self.vars["flavor_name"]
            if flavor_key == "":
                  break
            if flavor_key =="admin":
                  break
            if flavor_key in flavor_value :
                click_button(self,By.XPATH,"//tr[%s]/td/span/span/input"% str(i),"","click checkbox")
                count=count+1
                logging.info("---------click the checkbox -------")
          if count>0:
              return True 
          else :
              return False
      except:
        logging.error("user not found")
        self.driver.quit()

def create_project(self,project,cpuquota,memquota,gpuquota,description):
    ### setting project name and detail
    click_button(self,By.XPATH,"//span[contains(.,'Create Project')]","Create Project","Click project button")
    set_text(self,By.XPATH,"//input[@name='name']",project,"Set project name project=%s" %(project))
    set_text(self,By.XPATH,"//input[@name='desc']",description,"Set description project=%s" % (project))    
    ### setting project quota
    set_text(self,By.XPATH,"//input[@name='cpuQuota']",cpuquota,"Set cpuQuota=%s project=%s" % (cpuquota,project))
    set_text(self,By.XPATH,"//input[@name='memoryQuota']",memquota,"Set memoryQuota=%s project=%s" % (memquota,project))
    set_text(self,By.XPATH,"//input[@name='gpuQuota']",gpuquota,"Set gpuQuota =%s project=%s " % (gpuquota,project))
    ### disable openstack module
    openstack_status="return document.evaluate('//div[3]//div[1]//label[1]//span[1]//span[1]', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.outerHTML.length"
    if int(self.driver.execute_script(openstack_status)) > 380:
      click_button(self,By.XPATH,"//input[@name='module_5']","","Disable openstack")
    ### submit
    click_button(self,By.XPATH,"//span[contains(.,'Submit')]","Submit","Submit project")

    error_message=get_text(self,By.XPATH,"//span/div/div/div/div[1]","Get create project message")
    if error_message !="":
      error_message=get_text(self,By.XPATH,"//span/div/div/div/div[2]","Get error message")
      if error_message == "\"PROJECT NAME ALREADY EXIST\"":
        logging.warning("%s", error_message)
        return True
      logging.error("Create project error = %s", error_message)
      return False
    return True

def delete_project(self,project):
      try:
          for i in range(1, 50, 1):
            user_target = "//tr[%d]/td[2]/span" % (i)
            username=(get_text(self,By.XPATH,user_target,"Get project name"))
            logging.info("get project name = %s",username)
            user_select = "//tr[%d]/td[1]/span" % (i)
            
            if username =="":
              break
            if project == "admin":
              break
            if username == project:
              click_button(self,By.XPATH,user_select,"","user select")
              return True
          return False
      except:
        logging.error('user not found = %s',project)
        self.driver.quit()

def create_solution(self,i):
      try:
          click_button(self,By.XPATH,"//span[contains(text(),'Create Solution')]","Create Solution","click Create Solution button,")
          logging.info("---------create solution-------")
          set_text(self,By.XPATH,"//input[@placeholder='Please Enter Solution Name']",self.vars["solution"][i],"input solution name")
          click_button(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]","","click category button,")
          click_button(self,By.XPATH,"//div[2]/ul/li[2]","container","click container")
          time.sleep(0.5)
          set_text(self,By.XPATH,"//input[@placeholder='Please Enter Description']",self.vars["solution"][i],"input description name")
          click_button(self,By.XPATH,"//span[contains(text(),'Submit')]","Submit","submit,")
          logging.info("---------submit-------")
          time.sleep(4)
          # result = get_text(self,By.XPATH,"//span/div/div/div/div[2]","get Error message")
          # print(result)
          # if "already exists on default_k8s" in result:
          #     logging.warning("flavor name ALREADY EXIST create")
          # else :
          #     logging.info("Create user finish create flavor_name=%s",self.vars["flavor_name"][i])
          # self.driver.refresh()  
      except :
        logging.error("Can't create solution")

def delete_solution(self):
      count=0
      try:
          for i in range(1, 50, 1):
            solution_key=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span/a"% (str(i),2),"search solution_key")
            solution_value=self.vars["solution"]
            if solution_key == "":
                  break
            if solution_key =="admin":
                  break
            if solution_key in solution_value :
                click_button(self,By.XPATH,"//tr[%s]/td/span/span/input"% str(i),"","click checkbox")
                count=count+1
                logging.info("---------click the checkbox -------")
          if count>0:
              return True 
          else :
              return False
      except:
        logging.error("user not found")


def enble_project_solution(self,slidc_button1,solution_select1):
    
          try:
              slide_button=slidc_button1
              solution_select=solution_select1
              time.sleep(2)                
              if int(self.driver.execute_script(slide_button)) >= 27 and int(self.driver.execute_script(slide_button)) <=40:
                  click_button(self,By.XPATH,solution_select,"","click enable bar")
                  time.sleep(2)            
              time.sleep(5)              
          except:
            logging.error("click enable bar error")
    


        

   
    
    

