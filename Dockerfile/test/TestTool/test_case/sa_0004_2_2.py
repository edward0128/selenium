import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import pytest
from TestTool.control import *
from TestTool.task import *

def sa_0004_2_2_goto(self):
    assert connect_web(self,"test-sa-0004") == True
    assert login_web(self,self.vars["account_user"][0],self.vars["account_password"][0]) == True
    assert check_text(self,By.XPATH,"//li[2]/div/span/span","Infrastructure","Find Infrastructure") == True
    assert click_button(self,By.XPATH,"//li[2]/div/span/span","Infrastructure","click Infrastructure") == True
    assert check_text(self,By.XPATH,"//ul[@id='/admin/infra_mgmt$Menu']/li","Host","Find Host") == True
    assert click_button(self,By.XPATH,"//ul[@id='/admin/infra_mgmt$Menu']/li","Host","click Host") == True
    #assert click_button(self,By.XPATH,"/html/body/div[1]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]/div[1]/div/div/div","default_k8s","click Host") == True
    #assert click_button(self,By.XPATH,"/html/body/div[3]/div[2]/ul/li[3]","default_openstack","click Host") == True


def sa_0004_2_2_check(self):
    host_dict = {}

    for i in range(1, 10, 1):
      host_name=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span" % (str(i),1),"Get host name")
      if host_name =="":
        break
      assert check_text(self,By.XPATH,"//tr[%s]/td[%s]/span" % (str(i),2),"Up"," Check host status") == True
      host_dict[host_name]=get_text(self,By.XPATH,"//tr[%s]/td[%s]/span" % (str(i),4),"Save host to the dict %s" %(host_name))

    count=0
    for host in self.vars["k8s_name"]:
      logging.info('Check host %s',host)
      assert host in host_dict
      logging.info('Check ip %s',self.vars["k8s_ip"][count])
      assert host_dict[host] == self.vars["k8s_ip"][count]
      count=count+1