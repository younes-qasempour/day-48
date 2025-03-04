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

# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, "submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(documentation_link.text)
# bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.get_attribute('href'))

# My solution
x = driver.find_element(By.CSS_SELECTOR, ".event-widget div")
y = x.text.split("\n")[2:]
k = y[::2]
j = y[1::2]
t = {}
for i in range(len(k)):
    t.update({i:{"time": k[i], "name":j[i]}})
# print(t)

# Angela's solution
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
# for time in event_times:
#     print(time.text)
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
# for name in event_names:
#     print(name.text)
events = {}
for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)






# close: Closes a tab
# driver.close()
# quit: quit the entire browser
driver.quit()
