from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

import pandas as pd

# Config
login_time = 30  # Time for login (in seconds)
new_msg_time = 5  # TTime for a new message (in seconds)
send_msg_time = 5  # Time for sending a message (in seconds)
country_code = 91  # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
with open('message.txt', 'r') as file:
    msg = quote(file.read())

# Open browser with default link
link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)

# Loop Through Numbers List
numbers = pd.read_csv('numbers.csv')
numbers['first_name'] = numbers['name'].apply(lambda x: str(x).split(' ')[0])

for i in numbers.index:
    contact = numbers.iloc[i]
    first_name = contact['first_name']
    number = contact['number']
    mess = msg.replace("FULLNAME", first_name)
    link2 = f'https://web.whatsapp.com/send/?phone={country_code}{number}&text={mess}'
    driver.get(link2)
    time.sleep(new_msg_time)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(send_msg_time)
    print(f"Done for name: {first_name} with number: {number}")

# Quit the driver
driver.quit()
