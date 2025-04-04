from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

#username = input()
#password = input()

service = Service(executable_path="/Users/danielhe/Desktop/Projects/farming/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://osu.ppy.sh/community/forums/topics/2047212?n=1cl")
soup = BeautifulSoup(driver.page_source, 'html.parser')

info = soup.find_all('a', class_="forum-post-info__row forum-post-info__row--username js-usercard")[-1]
print(info.get_text())
print(info.get('data-user-id'))

button = driver.find_element(By.CLASS_NAME, "avatar--nav2")
button.click()

User = driver.find_element(By.NAME, "username")
username = input()
User.send_keys(username)
Pass = driver.find_element(By.NAME, "password")
password = input()
Pass.send_keys(password)

time.sleep(20)

driver.quit()
