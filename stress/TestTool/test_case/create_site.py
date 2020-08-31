import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def create_site_goto(self):
    assert connect_web(self,"test_create_site") == True
    assert login_web(self,self.vars["stress_user"],"password") == True

    logging.info('Go to container service')
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/ul/li[2]/ul/li[1]/div[1]/span/span","Container","Click Container") == True
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[1]/div/ul/li[2]/ul/li[1]/ul/li/span/span","Container Service","Click Container Service") == True
    return True
    
def create_site_create(self):
    logging.info('Create Container site')
    self.driver.refresh()
    assert click_button(self,By.XPATH,"//span[contains(text(),'Create Container Site')]","Create Container Site","Create Container Site") == True
    assert click_button(self,By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[1]/div/div/div","","Create Container Site") == True
    assert click_button(self,By.XPATH,"/html/body/div[3]/div[2]/ul/li[1]","tensorflow_gpu_classroom","Create Container Site") == True

    
    assert click_button(self,By.XPATH,"/html/body/div[2]/div[2]/div[2]/div[1]/div/div[2]/button[2]/span[1]","Submit","click submit") == True
    assert set_text(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/input","","click submit") == True
    
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/input").clear()
    assert set_text(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[1]/div/input",self.vars["stress_user"],"click submit") == True
    
    self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/input").clear()
    assert set_text(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[2]/div/input",self.vars["stress_user"],"click submit") == True
    
    
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div[3]/button[2]/span[1]","Next","click submit") == True
    assert set_text(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[1]/div/input","password","click submit") == True
    #assert set_text(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/div/input","80","click submit") == True
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div[4]/button[2]/span[1]","Next","click next") == True
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[3]/button[2]/span[1]","Submit","click submit") == True
    
    
    return True

def create_site_check(self):
    self.driver.refresh()
    dict_site={}
    try:                                      
        for i in range(1, 100):               
            #site_name=get_text(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[%d]/table/tbody/tr/td[2]/span/a" % (i),"get site name")    
            #site_status=get_text(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[%d]/table/tbody/tr/td[3]/span/a" % (i),"get site status")
            site_name=get_text(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[%d]/td[2]/span/a" % (i),"get site name")    
            site_status=get_text(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr[%d]/td[3]/span" % (i),"get site status")
            logging.info(site_status)           
            if site_status == "":
                break
            dict_site[site_name]=site_status
    except:
        return False
    
    if self.vars["stress_user"] in dict_site:
        if dict_site[self.vars["stress_user"]] == "Ready":
            return True
    return False
        


def create_site_delete(self):
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/table/tbody/tr/td[1]/span/span[1]/input","","click Submit") == True
    time.sleep(3)
    assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]/div[2]/button/span[1]/i","","click Submit") == True
    print("create_site_delete")
    return True