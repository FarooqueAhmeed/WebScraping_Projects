from selenium import webdriver
import webbrowser
from time import sleep
from selenium.webdriver.common.keys import Keys
# Specifying incognito mode as you launch your browser[OPTIONAL]
from setuptools.command.setopt import option_base
option = webdriver.ChromeOptions()
option.add_argument("--incognito")
# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
'''  # Go to desired website
browser.get("https://news.google.com")  '''

browser.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
username.send_keys("030883370")
password.send_keys("***")
submit   = browser.find_element_by_id("loginbutton")
#Last Step) Click Login
submit.click()

browser.implicitly_wait(20)
Search = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[3]/label/input").send_keys("Farooque Ahmed", Keys.ENTER)
find = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/span/div/div/a").send_keys(Keys.ENTER)




''' browser.implicitly_wait(20)
browser.quit()  '''

