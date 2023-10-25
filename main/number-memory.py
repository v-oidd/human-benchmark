"""
Bot for https://humanbenchmark.com/tests/number-memory
This will open a chrome tab where you are not signed in
Press Ctrl+C and log in to save your results
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

browser_options = Options()
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=browser_options)
driver.get("https://humanbenchmark.com/tests/number-memory")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]')))
start_button.click()

try:
	while True:
		number = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'big-number'))).get_attribute('innerText')

		text_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@pattern='[0-9]*' and @type='text']")))
		text_input.send_keys(number)

		submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Submit"]')))
		submit_button.click()

		next_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="NEXT"]')))
		next_button.click()
except KeyboardInterrupt:
	print("Bot stopped.")