from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = "https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT"
driver.get(url)

def click_next_page():
    next_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "next-page"))
    )
    next_page_button.click()

try:
    while True:
        click_next_page()
        time.sleep(3)  
except KeyboardInterrupt:
    print("stop")
finally:
    driver.quit()
