"""
Bot for https://humanbenchmark.com/tests/memory
This will open a chrome tab where you are not signed in
Press Ctrl+C and log in to save your results
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

browser_options = Options()
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=browser_options)
driver.get("https://humanbenchmark.com/tests/memory")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]')))
start_button.click()

level = 3
square_flashes = []

try:
	while True:
		while len(square_flashes) < level:
			square_flashes = driver.find_elements(By.CSS_SELECTOR, 'div.active')
		
		time.sleep(2)
		
		for square in square_flashes:
			square.click()
		
		level += 1

except KeyboardInterrupt:
	print("Bot stopped.")
