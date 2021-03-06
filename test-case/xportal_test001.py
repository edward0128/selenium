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

class DemoTest():
  def setup_method(self):
    # Start the logging
    
    logging.basicConfig(filename='program.log',format='%(levelname)s %(asctime)s %(message)s', level=logging.INFO)
    logging.info('########################selenium test start ########################')
    logging.info('Logging app started')

    # prepare the web driver
    options = Options()
    #options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    #options.add_argument('--headless')
    #options.add_argument("test=/Users/yu-sung/Documents/ci/profile.test")
    #driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    
    # get file path
    self.vars={}
    
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")
    config = configparser.ConfigParser()
    config.read(configPath)
    self.vars["grid_servier_url"] = config.get("webdriver","server")
    self.vars["browser"] = config.get("webdriver","browser")
    self.vars["url"] = config.get("xportal","url")
    self.vars["k8s_name"] = config.get("k8s","k8s_name")
    self.vars["k8s_ip"] = config.get("k8s","k8s_ip")
    try:
      self.driver = webdriver.Remote(command_executor=self.vars["grid_servier_url"],desired_capabilities={'browserName': self.vars["browser"], 'javascriptEnabled': False})
    except:
      logging.error('Prepare webdriver error', exc_info=True)
      self.driver.quit()
    
    logging.info('Prepare webdriver Ready')
  def teardown_method(self):
    self.driver.quit()
    logging.info('########################selenium test stop #########################') 
    
  def DemoTest_1(self):
    ########################################    
    #Connet and login to the xportal System
    try:
      self.driver.get(self.vars["url"])
    except:
      logging.error('Connect to the Site Error', exc_info=True)
      logging.error("NOT PASS!!!!")
      self.driver.quit()

    try:
      logging.info('Start to login the WebSite')
      self.driver.find_element(By.CSS_SELECTOR, ".login").click()
      self.driver.find_element(By.NAME, "email").click()
      self.driver.find_element(By.NAME, "email").send_keys("admin")
      self.vars["password"] = "password"
      self.driver.find_element(By.NAME, "password").send_keys(self.vars["password"])
      self.driver.find_element(By.CSS_SELECTOR, ".jss82").click()
      self.driver.implicitly_wait(10)
      logging.info('login success')
    except:
      logging.error('Connect to the Site Error', exc_info=True)
      logging.error("NOT PASS!!!!")
      self.driver.quit()
    
    ########################################
    delayTime=1
    try:
      logging.info('Click Infrastructure')
      infastructure=self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/ul[1]/li[1]/ul[1]/li[2]/div[1]/span[1]")  
      if infastructure.text == "Infrastructure":
        ActionChains(self.driver).move_to_element(infastructure).click(infastructure).perform()
        time.sleep(delayTime)
    except:
      logging.error('Click Infrastructure Error', exc_info=True)
      logging.error("NOT PASS!!!!")
      self.driver.quit()
    ########################################
    try:
      logging.info('Click Host')
      host=self.driver.find_element(By.XPATH, "//ul[@id='/admin/infra_mgmt$Menu']/li")
      if host.text == "Host":
        ActionChains(self.driver).move_to_element(host).click(host).perform()
      time.sleep(delayTime)
    except:
      logging.error('Click Host', exc_info=True)
      logging.error("NOT PASS!!!!")
      self.driver.quit()
    ########################################
    try:
      logging.info('Check Infrastructure Host')
      host=self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td/span/a")
      if host.text == self.vars["k8s_name"]:
        logging.info('Check Infrastructure Host OK %s == %s',host.text,self.vars["k8s_name"])
      else:
        logging.error('Check Infrastructure Host error %s != %s',host.text,self.vars["k8s_name"])
        logging.error("NOT PASS!!!!")
        self.driver.quit()
      
      host_status=self.driver.find_element(By.XPATH, "//div[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[2]/span")
      if host_status.text == "Up":
        logging.info('Check Host Staus OK %s == Up', host_status.text)
      else:
        logging.error('Check Host Staus Error %s != Up', host_status.text)
        logging.error("NOT PASS!!!!")
        self.driver.quit()  

      host_ip=self.driver.find_element(By.XPATH, "//td[4]/span")
      if host_ip.text == self.vars["k8s_ip"]:
        logging.info('Check Host_ip Ok %s == %s', host_ip.text,self.vars["k8s_ip"])
      else:
        logging.error('Check Host_ip Error %s != %s', host_ip.text,self.vars["k8s_ip"])
        logging.error("NOT PASS!!!!")
        self.driver.quit()  
    
      logging.info("PASS!!!!")
    except:
      logging.error("NOT PASS!!!!")
      self.driver.quit()    

    
    time.sleep(5)
  

if __name__ == "__main__":
  driver = DemoTest()
  driver.setup_method()
  driver.DemoTest_1()
  driver.teardown_method()