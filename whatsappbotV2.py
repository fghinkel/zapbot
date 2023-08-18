from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import time

def main():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get('https://web.whatsapp.com/')

    # Wait for the user to log in
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'side')))

    contacts = ['Eu', 'Contas']
    message = 'Bom dia, segue promoções!'

    for contact in contacts:
        find_contact(driver, contact)
        send_message(driver, contact, message)
        time.sleep(6)

    driver.quit()

def find_contact(driver, contact):
    search_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[1]/p'))
    )
    search_field.click()
    search_field.send_keys(contact)
    search_field.send_keys(Keys.ENTER)

def send_message(driver, contact, message):
    message_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'))
    )
    message_field.click()
    message_field.send_keys(message)
    message_field.send_keys(Keys.ENTER)

    # Clear the search field to prepare for the next contact
    clear_search_field(driver)

def clear_search_field(driver):
    # Click on an unrelated element to trigger a blur event on the search field
    body = driver.find_element(By.TAG_NAME, 'body')
    body.click()


if __name__ == "__main__":
    main()
