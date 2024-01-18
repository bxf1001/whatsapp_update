import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://eprisons.nic.in/TamilNadu/Secure/Login.aspx')


# find username/email field and send the username itself to the input field

browser.find_element(By.ID, "txtUserid").send_keys("sppuzhal1")
# find password input field and insert password as well
browser.find_element(By.ID, "txtPassword").send_keys("sppuzhal11")
browser.find_element(By.ID, "btnLogin").click()
browser.find_element(By.PARTIAL_LINK_TEXT, "Administration").click()
time.sleep(0.5)
browser.find_element(By.PARTIAL_LINK_TEXT, "Online Visit Approval").click()
time.sleep(0.5)
browser.find_element(By.LINK_TEXT, "VideoConferencing").click()

browser.find_element(By.CLASS_NAME, "chosen-single").click()
time.sleep(50) # sleep for 5 seconds so you can see the results
browser.quit()
