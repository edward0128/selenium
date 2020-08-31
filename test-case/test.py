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
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")
    config = configparser.ConfigParser()
    config.read(configPath)
    grid_servier_url = config.get("webdriver","server")
    browser = config.get("webdriver","browser")    
    try:
      self.driver = webdriver.Remote(command_executor=grid_servier_url,desired_capabilities={'browserName': browser, 'javascriptEnabled': False})
    except:
      logging.error('Prepare webdriver error', exc_info=True)
      self.driver.quit()
    
    self.vars={}
    self.vars["browser"] = config.get("webdriver","browser")
    logging.info('Prepare webdriver Ready')
  def teardown_method(self):
    self.driver.quit()
    logging.info('########################selenium test stop ########################') 
    
  def DemoTest_1(self):  
    #Connet and login to the xportal System
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, "config.ini")
    config = configparser.ConfigParser()
    config.read(configPath)
    url = config.get("xportal","url")
    k8s_name = config.get("k8s","k8s_name")
    k8s_ip = config.get("k8s","k8s_ip")

    print(self.vars["browser"])
    try:
      self.driver.get(url)
    except:
      logging.error('Connect to the Site Error', exc_info=True)
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
    except:
      logging.error('Connect to the Site Error')
      self.driver.quit()
    
    delayTime=1
    ########################################
    try:
      logging.info('Click Users')
      users=self.driver.find_element(By.XPATH, "//ul[@id='/admin$Menu']/li[3]/div")
      if users.text == "Users":
        ActionChains(self.driver).move_to_element(users).click(users).perform()
      time.sleep(delayTime)
    except:
      logging.error('Click Users')
      self.driver.quit()
    ########################################
    try:
      logging.info('Click usermanagement')
      usermanagement=self.driver.find_element(By.XPATH, "//ul[@id='/admin/user_mgmt$Menu']/li")
      if usermanagement.text == "User Management":
        ActionChains(self.driver).move_to_element(usermanagement).click(usermanagement).perform()
      time.sleep(delayTime)
    except:
      logging.error('Click usermanagement')
      self.driver.quit()

    #test=self.driver.find_element(By.XPATH, "//td[3]/span")
    #print(test.text)

    try:
      for i in range(2, 10, 1):
        print(i)
        #test2="(//a[contains(@href, '#/admin/user_mgmt/users')])["
        #test2+=i
        #test2+="]"
        #print(test2)
        #print(self.driver.find_element(By.XPATH, test2).text)
        
     
    except:
      print("error")
    
    #test=self.driver.find_element(By.XPATH, "(//a[contains(@href, '#/admin/user_mgmt/users')])[3]")
    #print(test.text)
    #test=self.driver.find_element(By.XPATH, "(//a[contains(@href, '#/admin/user_mgmt/users')])[4]")
    #print(test.text)
    
    
    ########################################
#//div[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr/td[3]/span
#//div[@id='root']/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/table/tbody/tr[2]/td[3]/span/a
#xpath=(//a[contains(@href, '#/admin/user_mgmt/users')])[2]
#time.sleep(10)
  

if __name__ == "__main__":
  driver = DemoTest()
  driver.setup_method()
  driver.DemoTest_1()
  driver.teardown_method()