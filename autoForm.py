from ast import Return
from optparse import Option
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
option = webdriver.ChromeOptions()
option.add_argument("-incognito")
option.add_argument("disable-gpu")
fileDir = "formAuto.txt"
file = open(fileDir, "r")
lines = file.readlines()
username = lines[0]
password = lines[1]
email = lines[2]
chromeDirectory = lines[3]
#option.add_argument("--headless")
#option.add_argument("window-size=1920,1080")
browser = webdriver.Chrome(executable_path=chromeDirectory, options=option)

browser.get("https://docs.google.com/forms/d/e/1FAIpQLSfylX2OrLULh-f9tHJqY9NVanqOw-zRii500murmMqA4Pguuw/viewform")
time.sleep(1)

googleEmailLogin = browser.find_element_by_id("identifierId")
googleEmailLogin.clear()
googleEmailLogin.send_keys(email)
googleEmailLogin.send_keys(Keys.RETURN)
print("Google Login done.")
time.sleep(1)
email = browser.find_element_by_id("UserName")
email.send_keys(username)
time.sleep(1)
passwordBox = browser.find_element_by_id("Password")
passwordBox.send_keys(password)
#passwordBox.send_keys(Keys.RETURN)
print("GAPPS login done.")
time.sleep(10)
textboxes = browser.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
textboxes[0].send_keys("Aaron")
textboxes[1].send_keys("Amelink")
print("name entered")
radiobuttons = browser.find_elements_by_class_name("docssharedWizToggleLabeledLabelWrapper")
radiobuttons[0].click()

submitbutton = browser.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
submitbutton[2].click()
time.sleep(2)
browser.close()
print("done.")
