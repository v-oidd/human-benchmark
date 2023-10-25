# Bot for https://humanbenchmark.com/tests/sequence
# To stop the bot, press Ctrl+C - the website will stay open

browser_options = Options()
browser_options.add_experimental_option('excludeSwitches', ['enable-logging'])
browser_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=browser_options)
driver.get("https://humanbenchmark.com/tests/chimp")

cookie_popup = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="AGREE"]')))
cookie_popup.click()

start_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Start Test"]')))
start_button.click()

buttonCount = 4
buttons = []

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
