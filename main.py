from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is ${price_dollar.text}.{price_cents.text}")

search_bar = driver.find_element(By.NAME, "q")
print(search_bar)

# close: Closes a tab
# driver.close()
# quit: quit the entire browser
driver.quit()
