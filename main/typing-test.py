"""
Bot for https://humanbenchmark.com/tests/typing
This will open a chrome tab where you are not signed in
Log in before starting the bot to save your results
Press 's' while on the start menu to start the bot
Press Ctrl+C and log in to save your results
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import keyboard

user_start_button = 's'

browser_options = Options()
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=browser_options)
driver.get("https://humanbenchmark.com/tests/typing")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

keyboard.wait(user_start_button)

try:
	while True:
		# Select text box
		text_box = driver.find_element(By.CLASS_NAME, "notranslate")
		text_box.click()

		# Get text to write
		letters = driver.find_elements(By.CLASS_NAME, "incomplete")
		text = "".join([letter.get_attribute('innerText') for letter in letters])

		keyboard.write(text)

		WebDriverWait(driver, 99999).until(EC.element_to_be_clickable((By.CLASS_NAME, "notranslate")))
except KeyboardInterrupt:
	print("Bot stopped.")
