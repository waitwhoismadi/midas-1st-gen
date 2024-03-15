# from selenium import webdriver
# from bs4 import BeautifulSoup

# driver = webdriver.Chrome()
# url = 'https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT'
# driver.get(url)
# driver.implicitly_wait(10)
# html_code = driver.page_source
# soup = BeautifulSoup(html_code, 'html.parser')
# last_page_button = soup.find('button', {'class': 'css-hlqxzb'})
# last_page_number = int(last_page_button.text)
# print("Last Page Number:", last_page_number)
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = 'https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT'
driver.get(url)
driver.implicitly_wait(10)
sixth_button = driver.find_element(By.XPATH, '(//div[@class="css-b0tuh4"]//button)[6]')
sixth_button_text = sixth_button.text
print("Text from the sixth button:", sixth_button_text)    

driver.quit()
