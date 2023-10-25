"""
Bot for https://humanbenchmark.com/tests/chimp
This will open a chrome tab where you are not signed in
Log in before starting the bot to save your results
Press 's' while on the start menu to start the bot
Press Ctrl+C to stop the bot - the tab will stay open
NOTE: 41 is the maximum possible score
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
driver.get("https://humanbenchmark.com/tests/chimp")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

keyboard.wait(user_start_button)

start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Start Test"]')))
start_button.click()

buttonCount = 4
buttons = []

try:
	while True:
		for i in range(1, buttonCount+1):
			buttons.append(driver.find_element(By.XPATH, f'//div[@data-cellnumber={str(i)}]'))
		for button in buttons:
			button.click()
		# Increment by 1 as the next level will have 1 more button
		buttonCount += 1
		buttons.clear()

		continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue"]')))
		continue_button.click()
except KeyboardInterrupt:
	print("Bot stopped.")
