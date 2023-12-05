import requests
from bs4 import BeautifulSoup


class PublicoWebScraper:
    def __init__(self, urls):
        self.urls = urls
        self.data = []

    def fetch_data(self) -> None:
        for url in self.urls:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                articles = soup.find_all(['h3', 'h4'])

                for article in articles:
                    title_text = article.get_text(strip=True)

                    if title_text:
                        self.data.append({'title': title_text, 'category': url})

    def save_to_file(self, filename) -> None:
        with open(filename, 'w', encoding='utf-8') as file:
            for entry in self.data:
                file.write(f"{entry['category']}: {entry['title']}\n\n")
