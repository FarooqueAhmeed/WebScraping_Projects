from selenium import webdriver
import webbrowser
from time import sleep
from selenium.webdriver.common.keys import Keys
# Specifying incognito mode as you launch your browser[OPTIONAL]
from setuptools.command.setopt import option_base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




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
username.send_keys("03088337062")
password.send_keys("Fah")
submit   = browser.find_element_by_id("loginbutton")
#Last Step) Click Login
submit.click()

browser.implicitly_wait(20)
Search = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/div/div/div/div[3]/label/input").send_keys("Farooque Ahmed", Keys.ENTER)
try:
    element = WebDriverWait(webdriver, 10).until(
        EC.element_to_be_clickable((By.ID, "myDynamicElement"))
    )
finally:
    pClick = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.rj1gh0hx.buofh1pr.g5gj957u.hpfvmrgz.dp1hu0rb > div > div > div > div > div > div > div:nth-child(1) > div > div > div > div:nth-child(1) > div.dhix69tm.sjgh65i0.wkznzc2l.tr9rh885 > div.qu0x051f.f10w8fjw.jb3vyjys > div > div > div.tvfksri0.taijpn5t.j83agx80.ll8tlv6m > div > div > div > svg > g > image").click()
try:
    element = WebDriverWait(webdriver, 10).until(
        EC.element_to_be_clickable((By.ID, "myDynamicElement"))
    )
finally:
    msgClick = browser.find_element_by_css_selector("#mount_0_0 > div > div > div.rq0escxv.l9j0dhe7.du4w35lb > div > div > div.j83agx80.cbu4d94t.d6urw2fd.dp1hu0rb.l9j0dhe7.du4w35lb > div > div > div > div.rq0escxv.lpgh02oy.tkr6xdv7.rek2kq2y > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.gs1a9yip.owycx6da.btwxx1t3.cddn0xzi.dsne8k7f > div > div > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.cbu4d94t.d2edcug0.o8rfisnq > div > div > div:nth-child(2) > div > span > div > div.rq0escxv.l9j0dhe7.du4w35lb.j83agx80.taijpn5t.bp9cbjyn.owycx6da.btwxx1t3.c4xchbtz.by2jbhx6 > div > img").click()


''' browser.implicitly_wait(20)
browser.quit()  '''

