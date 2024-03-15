from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service


url = 'https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT'


def write_to_csv(data):
    with open('p2p_offers.csv', mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['URL', 'All trades', '30d trades', '30d completion rate', 'Avg. release time', 'Avg. pay time']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        for row in data:
            writer.writerow(row)


def scrape_p2p_data_1exq9ec(driver):
    data = []
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'tbody')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    p2p_offers = soup.find_all('tbody', class_='bn-table-tbody')

    for offer in p2p_offers:
        a_tags = offer.find_all('a', id="")
        for a_tag in a_tags:
            href = a_tag.get('href')
            final_url = urljoin(url, href)
            driver.get(final_url)
            try:
                # Only changing class='css-3njx2k' to a more general approach
                all_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[contains(@class, 'css-')][contains(text(),'All Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_trades = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[contains(@class, 'css-')][contains(text(),'30d Trades')]/following-sibling::div//span[@class='css-1exq9ec']").text
                thirtyD_completion_rate = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[contains(@class, 'css-')][contains(text(),'30d Completion Rate')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_release_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[contains(@class, 'css-')][contains(text(),'Avg. Release Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                avg_pay_time = driver.find_element(By.XPATH, "//div[@class='css-1tngqys']//div[contains(@class, 'css-')][contains(text(),'Avg. Pay Time')]/following-sibling::div//span[@class='css-1exq9ec']").text
                data.append({
                    'URL': final_url,
                    'All trades': all_trades,
                    '30d trades': thirtyD_trades,
                    '30d completion rate': thirtyD_completion_rate,
                    'Avg. release time': avg_release_time,
                    'Avg. pay time': avg_pay_time,
                })
            except NoSuchElementException:
                print("Elements could not be found for URL:", final_url)
            except Exception as e:
                print(f"Error occurred: {e}")
            time.sleep(1)

    return data
# с помощью контента ищу спан, в котором содержится avg time и т.д. 

def click_confirm_button():
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')  
    service = Service(executable_path='./chromedriver.exe')

    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(url) 

    sixth_button = driver.find_element(By.XPATH, '(//div[@class="css-b0tuh4"]//button)[6]')
    sixth_button_text = sixth_button.text
    last_page = int(sixth_button_text)   

    try:
        current_page = 1
        scraped_user_pages = 0

        while scraped_user_pages < last_page:  
            scraped_data = scrape_p2p_data_1exq9ec(driver)
            write_to_csv(scraped_data)

            scraped_user_pages += 1
            i = 0
            
            driver.get(url)
            while i < current_page:
                driver.get(url)
                next_page_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "next-page"))
                )
                next_page_button.click()
                i += 1

            current_page += 1
            time.sleep(3)

    except KeyboardInterrupt:
        print("Script stopped by the user.")
    finally:
        driver.quit()


click_confirm_button()

df = pd.read_csv('p2p_offers.csv')
print(df)

from bs4 import BeautifulSoup

url = url = 'https://p2p.binance.com/en/trade/all-payments/USDT?fiat=KZT'
soup = BeautifulSoup(url, 'html.parser')
last_page_button = soup.find('button', {'class': 'css-hlqxzb'})
last_page_number = int(last_page_button.text)
print("Last Page Number:", last_page_number)