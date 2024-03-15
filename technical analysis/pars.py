from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from urllib.parse import urljoin
import csv
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT'
driver.get(url)

def write_to_csv(data):
    with open('p2p_offers.csv', mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['URL', 'All trades', '30d trades', '30d completion rate', 'Avg. release time', 'Avg. pay time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
            
def scrape_p2p_data_1exq9ec(driver):
    data = []
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'tbody')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    p2p_offers = soup.find_all('tbody', class_='bn-table-tbody')
    
    for offer in p2p_offers:
        a_tags = offer.find_all('a', id="")  
        for a_tag in a_tags:
            href = a_tag.get('href')
            final_url = urljoin(url, href)
            driver.get(final_url)
            try:
                all_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-1t6ikjh'][contains(text(),'All Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-1t6ikjh'][contains(text(),'30d Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_completion_rate = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-1t6ikjh'][contains(text(),'30d Completion Rate')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_release_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-1t6ikjh'][contains(text(),'Avg. Release Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_pay_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-1t6ikjh'][contains(text(),'Avg. Pay Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                data.append({
                    'URL': final_url,
                    'All trades': all_trades,
                    '30d trades': thirtyD_trades,
                    '30d completion rate': thirtyD_completion_rate,
                    'Avg. release time': avg_release_time,
                    'Avg. pay time': avg_pay_time,
                })
            except NoSuchElementException:
                all_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-youqw8'][contains(text(),'All Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-youqw8'][contains(text(),'30d Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_completion_rate = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-youqw8'][contains(text(),'30d Completion Rate')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_release_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-youqw8'][contains(text(),'Avg. Release Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_pay_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[@class='css-youqw8'][contains(text(),'Avg. Pay Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                data.append({
                    'URL': final_url,
                    'All trades': all_trades,
                    '30d trades': thirtyD_trades,
                    '30d completion rate': thirtyD_completion_rate,
                    'Avg. release time': avg_release_time,
                    'Avg. pay time': avg_pay_time,
                })
                print("Some elements could not be found on the page.")
                print(final_url)
            except Exception as e:
                print(f"Error occurred: {e}")
            time.sleep(2)
    return data



def click_confirm_button():
    driver = webdriver.Chrome()
    try:
        scraped_data = scrape_p2p_data_1exq9ec(driver)
        write_to_csv(scraped_data)
    finally:
        driver.quit()

def click_next_page():
    driver.get("https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT")
    driver.find_element(By.ID, "next-page").click()

click_confirm_button()
df = pd.read_csv('p2p_offers.csv')
df