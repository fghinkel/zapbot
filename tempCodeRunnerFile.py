# Version's
# Python version: 3.8.5
# selenium version: 3.141.0
# webdriver_manager: 3.2.2

# Importing lib's

from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

# Defining webdriver configuration
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

# Defining contacts and groups to send the message
contacts = ['Eu', 'Julinda']