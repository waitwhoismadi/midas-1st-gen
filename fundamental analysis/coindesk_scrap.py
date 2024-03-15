import requests
from bs4 import BeautifulSoup
import csv

def scrape_coindesk_news():
    url = "https://www.coindesk.com/livewire"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("article", class_="heading")
    scraped_data = []

    for article in articles:
        title = article.find("h3", class_="heading").text.strip()
        author = article.find("a", class_="author").text.strip()
        time = article.find("time")["datetime"]
        article_url = article.find("a")["href"]
        article_response = requests.get(article_url)
        article_soup = BeautifulSoup(article_response.content, "html.parser")
        content = article_soup.find("div", class_="post-content").text.strip()

        scraped_data.append([title, author, content, time])

    with open("coindesk_news.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Title", "Author", "Content", "Time"])
        csv_writer.writerows(scraped_data)

if __name__ == "__main__":
    scrape_coindesk_news()
