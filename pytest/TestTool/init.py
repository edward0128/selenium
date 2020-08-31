import logging
import configparser
import os
from selenium import webdriver
import time
def init_log(logPath,level):
    logging.basicConfig(filename="/Users/yu-sung/Documents/ci/gmn-1.0.46-autotesting/selenium/test-case/selenium.log",format='%(levelname)s %(asctime)s %(message)s', level=level)
    logging.info('Logging app started')

def start_test(testcase):
    testcase_split=testcase.split(".py")
    logging.info('######################%s start######################',testcase_split[0])
    time.sleep(2)

def end_test(testcase):
    testcase_split=testcase.split(".py")
    logging.info('######################%s end########################',testcase_split[0])
    logging.info('######################%s pass#######################',testcase_split[0])
    time.sleep(2)

def init_driver(self):
    try:
        logging.info("Start init webdriver")
        driver=webdriver.Remote(command_executor=self.vars["grid_servier_url"],desired_capabilities={'browserName': self.vars["browser"], 'javascriptEnabled': False})
        driver.implicitly_wait(10)
        return driver
    except:
        driver.quit()
        logging.error('Prepare webdriver error', exc_info=True)

def read_config(file_object,config_path):
    proDir = os.path.split(os.path.realpath(__file__))[0]
    configPath = os.path.join(proDir, config_path)
    config = configparser.ConfigParser()
    config.read(configPath)
    file_object.vars["grid_servier_url"] = config.get("webdriver","server")
    file_object.vars["browser"] = config.get("webdriver","browser")
    file_object.vars["url"] = config.get("xportal","url")
    file_object.vars["k8s_name"] = config.get("k8s","k8s_name").split(",")
    file_object.vars["k8s_ip"] = config.get("k8s","k8s_ip").split(",")
    file_object.vars["DelayTime"] = config.get("config","DelayTime")
    file_object.vars["account_user"] = config.get("account","account").split(",")
    file_object.vars["account_password"] = config.get("account","password").split(",")
    file_object.vars["project_name"] = config.get("project","project_name").split(",")
    file_object.vars["project_description"] = config.get("project","project_description").split(",")
    file_object.vars["project_quota_cpu"] = config.get("project","project_quota_cpu").split(",")
    file_object.vars["project_quota_mem"] = config.get("project","project_quota_mem").split(",")
    file_object.vars["project_quota_gpu"] = config.get("project","project_quota_gpu").split(",")

    file_object.vars["flavor_name"] = config.get("flavor","flavor_name").split(",")
    file_object.vars["flavor_cpu"] = config.get("flavor","flavor_cpu").split(",")
    file_object.vars["flavor_memory"] = config.get("flavor","flavor_memory").split(",")
    file_object.vars["flavor_disk"] = config.get("flavor","flavor_disk").split(",")
    file_object.vars["flavor_gpu"] = config.get("flavor","flavor_gpu").split(",")
    file_object.vars["solution"] = config.get("solution","solution_name").split(",")
    return file_object

