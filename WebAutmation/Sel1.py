from selenium import webdriver
import webbrowser
from time import sleep

# Specifying incognito mode as you launch your browser[OPTIONAL]
from setuptools.command.setopt import option_base

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)



'''  # Go to desired website
browser.get("https://news.google.com")  '''


'''    browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit   = browser.find_element_by_id("loginbutton")
username.send_keys("***********")
password.send_keys("**************")

search = browser.find_element_by_id("pass")

#Last Step) Click Login
submit.click()
  '''
