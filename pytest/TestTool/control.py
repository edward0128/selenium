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
def connect_web(self,alert_message):
      logging.info('Connect to the web site %s', self.vars["url"])
      self.driver.get(self.vars["url"])
      time.sleep(2)
      page_result=get_text(self,By.XPATH,"/html/body/div[1]/div/div/form/div[1]/label","get Account or Email")
      assert  page_result == "Account or Email"
      self.driver.execute_script("alert(\"%s\")" % (alert_message))
      time.sleep(2)
      self.driver.switch_to.alert.accept()
      return True


def login_web(self,account,password):
    try:
      logging.info("Try to login. user=%s password=%s ",account,password)
      self.driver.find_element(By.NAME, "email").send_keys(account)
      self.driver.find_element(By.NAME, "password").send_keys(password)
      self.driver.find_element(By.XPATH, "//span[contains(.,'Log In')]").click()
      time.sleep(2)
      logging.info('waiting for login 2 sec')
      
      login_message=get_text(self,By.XPATH,"/html/body/div[1]/div/div/form/span[1]","check login message")
      
      if login_message != "":
        logging.error('login error %s', login_message)
        return False      
      
      login_pop_up=get_text(self,By.XPATH,"//span/div/div/div/div","get pop up message.")
      
      if login_pop_up == "Warning":
        error_message=get_text(self,By.XPATH,"//div/div[2]","get pop up warning message")
        logging.warning("%s",error_message)
        time.sleep(10)
        return True
      else:
        logging.info("login success. user=%s ",account)
        return True
    except:
      logging.error('login error', exc_info=True)

def try_login_web(self,account,password):
    try:
      logging.info('Start to login the WebSite. user=%s password=%s',account,password)
      self.driver.find_element(By.CSS_SELECTOR, ".login").click()
      self.driver.find_element(By.NAME, "email").click()
      self.driver.find_element(By.NAME, "email").send_keys(account)
      self.driver.find_element(By.NAME, "password").send_keys(password)
      self.driver.find_element(By.XPATH, "//span[contains(.,'Log In')]").click()
      
      time.sleep(2)
      login_message=""
      login_message=get_text(self,By.XPATH,"/html/body/div[1]/div/div/form/span[1]","Get login error message.")
      
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
      
      target=self.driver.find_element(method,path)
      print(target.text)
      logging.info("%s .Target found. xpath=%s text=%s",log,path,target.text)
      highlight_check(target)
      return target.text
    except :
      logging.warning("%s. Target text notfound. xpath=%s",log,path)
      return ""
    

def set_text(self,method,path,input_text,log):
    try:
      target=self.driver.find_element(method, path)
      highlight_check(target)
      target.send_keys(input_text)
      logging.info("%s. input_text= %s",log,input_text)
      return True
    except:
      logging.error("%s. input error input_text= %s",log,input_text)
      return False

def check_text(self,method,path,target_text,log):
      target=self.driver.find_element(method, path)
      highlight_check(target)
      if target.text == target_text:
        logging.info('%s. Check success. target=%s',log,target.text)
        return True
      else:
        logging.error('%s .Target text not match. %s != %s',log,target_text,target.text)
        return False


def click_button(self,method,path,target_text,log):
    target=self.driver.find_element(method, path)
    highlight_click(target)
    try:
      if target.text == target_text:
        logging.info('%s Target match success %s = %s',log,target_text,target.text)
        ActionChains(self.driver).move_to_element(target).click(target).perform()
        return True
      else:
        logging.error('%s. Click target text not match %s != %s',log,target_text,target.text)
        return False
    except:
      logging.error('%s. Click target not found. %s != %s',log,target_text,target.text)
      return False

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


