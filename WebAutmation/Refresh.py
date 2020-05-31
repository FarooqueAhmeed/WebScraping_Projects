import webbrowser
from time import sleep
from selenium import webdriver

# Specifying incognito mode as you launch your browser[OPTIONAL]
from setuptools.command.setopt import option_base

option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='chromedriver.exe', options=option)


url = input('Input the URL to reload, including "http://: ')

while True:
    print("refreshing...")
    webbrowser.open(url, new=0)
    sleep(10)