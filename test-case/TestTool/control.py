import logging
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from pprint import pprint
from PIL import Image
import __main__
def connect_web(self):
    try:
      logging.info('Connect to the web site %s', self.vars["url"])
      self.driver.get(self.vars["url"])
      file_name=__main__.__file__
      test_case=file_name.split(".py")
      self.driver.execute_script("alert(\"%s\")" % (test_case[0]))
      time.sleep(2)
      self.driver.switch_to.alert.accept()
    except:
      logging.error('Connect to the Site error', exc_info=True)
      logging.error("Site url = %s",self.vars["url"])
      self.driver.quit()

def login_web(self,account,password):
    try:
      logging.info('Start to login the webSite user=%s',account)
      self.driver.find_element(By.CSS_SELECTOR, ".login").click()
      self.driver.find_element(By.NAME, "email").click()
      self.driver.find_element(By.NAME, "email").send_keys(account)
      self.driver.find_element(By.NAME, "password").send_keys(password)
      self.driver.find_element(By.XPATH, "//span[contains(.,'Log In')]").click()
      
      login_message=get_text(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/span[1]","Get login error message")
      
      if login_message != "":
        logging.error('login error %s', login_message)
        raise "login_error"      
      
      login_pop_up=get_text(self,By.XPATH,"//span/div/div/div/div","check login message.")
      logging.info("Try to login. user=%s password=%s ",account,password)
      
      if login_pop_up == "Warning":
        error_message=get_text(self,By.XPATH,"//div/div[2]","check login message")
        logging.warning("%s",error_message)
        time.sleep(10)
        return False
      else:
        logging.info("login success. user=%s ",account)
        return True
    except:
      logging.error('login error', exc_info=True)
      self.driver.quit()

def test_login_web(self,account,password):
    try:
      logging.info('Start to login the WebSite. user=%s password=%s',account,password)
      self.driver.find_element(By.CSS_SELECTOR, ".login").click()
      self.driver.find_element(By.NAME, "email").click()
      self.driver.find_element(By.NAME, "email").send_keys(account)
      self.driver.find_element(By.NAME, "password").send_keys(password)
      self.driver.find_element(By.XPATH, "//span[contains(.,'Log In')]").click()
      
      login_message=get_text(self,By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/form[1]/span[1]","Get login error message.")
      
      if login_message != "":
        logging.error('Login error message message= %s.', login_message)
        raise "login_error"

      logging.info("Try to login. user=%s password=%s",account,password)
      login_pop_up=get_text(self,By.XPATH,"//span/div/div/div/div","Check login message")

      if login_pop_up == "Warning":
        error_message=get_text(self,By.XPATH,"//div/div[2]","check login message")
        logging.warning("%s",error_message)
        logging.info("%s","wait 10 sec")
        time.sleep(10)
        return True
      else:
        logging.info("login success user=%s ",account)
        logging.info("Start to logout")
        click_button(self,By.XPATH,"//div[4]/button/span/span[2]",account,"click %s button" % (account))
        click_button(self,By.XPATH,"//span[contains(.,'Log Out')]","Log Out","click logout button")
        return True
    except:
      logging.error('login error', exc_info=True)
      return False

def get_text(self,method,path,log):
    try:
      self.driver.implicitly_wait(3)
      logging.info(log)
      target=self.driver.find_element(method, path)
      highlight_check(target)
      return target.text
    except :
      logging.warning("Target text notfound. xpatch=%s",path)
      return ""

def set_text(self,method,path,input_text,log):
    try:
      logging.info(log)
      target=self.driver.find_element(method, path)
      highlight_check(target)
      target.send_keys(input_text)
    except :
      logging.warning("Set input text error. xpatch=%s",path)

def check_text(self,method,path,target_text,log):
    try:
      logging.info(log)
      target=self.driver.find_element(method, path)
      highlight_check(target)
      if target.text == target_text:
        logging.info('Check success. %s target=%s',log,target.text)
      else:
        logging.error('Target text not match. %s != %s',target_text,target.text)
        raise 'target name not match'
    except :
      logging.error("Check error can't get target. Target not match %s",target_text)
      self.driver.quit()

def click_button(self,method,path,target_text,log):
    try:
      logging.info(log)
      target=self.driver.find_element(method, path)
      highlight_click(target)

      if target.text == target_text:
        logging.info('Target match success %s = %s',target_text,target.text)
        ActionChains(self.driver).move_to_element(target).click(target).perform()
      else:
        logging.error('Click target text not match %s != %s',target_text,target.text)
        raise 'target not match' 
    except :
      logging.error("Can't click button target= %s",target_text)
      self.driver.quit()


def highlight_check(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: blue; border: 1px solid red;")
    time.sleep(0.1)
    apply_style(original_style)

def highlight_click(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: green; border: 1px solid red;")
    time.sleep(0.1)
    apply_style(original_style)

def image_recognition(self,method,path):
  try:
        image=self.driver.find_element(method,path)
        highlight_click(image)
        left = image.location['x']+ (image.size['width'])/2
        top = image.location['y']+ (image.size['height'])/2
        elementWidth = image.location['x']+ (image.size['width'])
        elementHeight = image.location['y']+ (image.size['height'])
        self.driver.get_screenshot_as_file('image.png')
        picture = Image.open('image.png')
        picture = picture.crop((left, top, elementWidth, elementHeight))
        pix = picture.load()
        picture.close()
        return pix
  except:      
        logging.error('Recognition error', exc_info=True)
        self.driver.quit()


