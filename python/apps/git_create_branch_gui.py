import subprocess
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

login_val="root"
pass_val=""

# Chromeの起動オプション
options = [
    r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    r'-remote-debugging-port=9222',
    r'--user-data-dir=C:\chromedata',
]
# Chromeを起動
process = subprocess.Popen(options, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, start_new_session=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
#url = 'http://192.168.0.19:20080/root/linux/-/branches/new'
url = r'http://192.168.0.19:20080/'
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
driver.get(url)

user_login = driver.find_element(By.XPATH, f'//*[@id="user_login"]')
user_login.send_keys(f"{login_val}")

user_pass = driver.find_element(By.XPATH, f'//*[@id="user_password"]')
user_pass.send_keys(f"{pass_val}")

signin_btn = driver.find_element(By.XPATH, f'//*[@id="new_user"]/button')
signin_btn.click()

for create_branch_name in [1,2,3,4,5,6,7,8,9,10]:
    url=r'http://192.168.0.19:20080/root/linux/-/branches/new'
    driver.get(url)

    branch_name = driver.find_element(By.XPATH, '//*[@id="branch_name"]')
    branch_name.send_keys(f"{create_branch_name}")

    branch_selector = driver.find_element(By.ID, "dropdown-toggle-btn-36")
    branch_selector.click()

    test_branch = driver.find_element(By.XPATH, "//li[@data-testid='listbox-item-main']")
    test_branch.click()

    time.sleep(1)

    create_branch_btn = driver.find_element(By.XPATH, '//*[@id="new-branch-form"]/button')
    create_branch_btn.click()
