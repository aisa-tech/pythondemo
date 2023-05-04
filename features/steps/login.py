import time
import os
import sys
from behave import *
import pyautogui as pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import wait, expected_conditions





@given(u'user should go homepage')
def step_impl(context):

  # Set up the browser with desired capabilities
  options = webdriver.ChromeOptions()
  options.add_argument("--start-maximized")

  # Create a new instance of the webdriver
  options.add_experimental_option("detach", True)
  context.driver = webdriver.Chrome(options=options)

  # Set the basic authentication credentials
  username = os.environ.get('username')

  password = os.environ.get('password')
  print(username)
  print(password)

  context.driver.get("google.com")
  #context.driver.get(configreader.)

  # Type the username and password into the relevant fields
  time.sleep(2)
  pyautogui.typewrite(username)
  time.sleep(2)
  pyautogui.press("tab")
  time.sleep(2)
  pyautogui.typewrite(password)

  # Click the submit button
  time.sleep(2)
  pyautogui.press("enter")




