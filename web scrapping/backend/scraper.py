import requests
from bs4 import BeautifulSoup

def get_news():
    news_sites = [
        "https://www.bbc.com/news",
        "https://www.reuters.com",
        "https://www.nytimes.com"
    ]
    
    all_news = []
    
    for site in news_sites:
        response = requests.get(site)
        soup = BeautifulSoup(response.text, 'html.parser')

        # BBC example scraping
        if "bbc" in site:
            headlines = soup.find_all('h3')
            for headline in headlines:
                link = headline.find('a')
                if link:
                    title = link.get_text()
                    url = link['href']
                    all_news.append({'title': title, 'content': "", 'link': url, 'source': "BBC"})
        
        # Add more scraping logic for other websites (Reuters, NY Times, etc.)
        # Similarly scrape the articles for each site

    return all_news
