"""
Bot for https://humanbenchmark.com/tests/sequence
This will open a chrome tab where you are not signed in
Press Ctrl+C and log in to save your results
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time

browser_options = Options()
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=browser_options)
driver.get("https://humanbenchmark.com/tests/sequence")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]')))
start_button.click()

square_grid = driver.find_element(By.CLASS_NAME, "squares")
square_rows = square_grid.find_elements(By.CLASS_NAME, "square-row")
squares = [square for square in square_rows]

square_flashes = []
last_time = time.time() + 100

try:
	while True:
		# If >1s has passed since last flash, begin clicking squares
		if time.time() - last_time > 1:
			for square in square_flashes:
				square.click()
			# Last time is resetted to prevent next time check from executing immediately
			last_time = time.time() + 100
			square_flashes.clear()
			continue
		try:
			current_flash = driver.find_element(By.CLASS_NAME, "square.active") 
			# Ensure current flash is different to last flash to avoid duplicate flashes
			if len(square_flashes) == 0 or current_flash != square_flashes[-1]:
				square_flashes.append(current_flash)
				last_time = time.time()
				
		except NoSuchElementException:
			continue
			
except KeyboardInterrupt:
	print("Bot stopped.")
