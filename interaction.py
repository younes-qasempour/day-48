from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# # article_count = driver.find_elements(By.CSS_SELECTOR, "#articlecount li a")
#
# # Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# # all_portals.click()
# search_click = driver.find_element(By.CSS_SELECTOR, ".mw-ui-icon-wikimedia-search")
# search_click.click()
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("HOY")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("YEE")
email = driver.find_element(By.NAME, "email")
email.send_keys("how-yee@gmail.com")
button = driver.find_element(By.CSS_SELECTOR, ".btn-lg")
button.click()























# driver.quit()