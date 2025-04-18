from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        top_news = scrape_top_news(url)
        latest_news = scrape_latest_news(url)
        return render_template('index.html', top_news=top_news, latest_news=latest_news)
    return render_template('index.html', top_news=None, latest_news=None)

def scrape_top_news(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, "html.parser")
        left_part = soup.find("div", class_="left-part", attrs={"data-tb-region": "home-top-news-list"})
        if left_part:
            other_articles = left_part.find_all("div", class_="other-article")
            news_list = []
            for article in other_articles:
                headline_tag = article.find("h3")
                headline_text = headline_tag.get_text(strip=True) if headline_tag else "No headline"
                link = (
                    headline_tag.find("a")["href"]
                    if headline_tag and headline_tag.find("a")
                    else "#"
                )
                news_list.append({"title": headline_text, "link": link})
            return news_list
        return [{"title": "No top news found.", "link": "#"}]
    except requests.exceptions.RequestException as e:
        return [{"title": f"Error fetching the URL: {e}", "link": "#"}]

def scrape_latest_news(url):
    try:
        # Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse the content using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the main div with class 'right-part bg'
        right_part = soup.find("div", class_="right-part bg")
        if right_part:
            # Find the 'top-news' div within this section
            top_news_div = right_part.find("div", class_="top-news")
            if top_news_div:
                # Find all <h3> tags containing news headlines
                headlines = top_news_div.find_all("h3")
                news_list = []
                for headline in headlines:
                    # Extract the text and the hyperlink
                    headline_text = headline.get_text(strip=True)
                    link = headline.find("a")["href"] if headline.find("a") else "#"
                    news_list.append({"title": headline_text, "link": link})
                return news_list
            else:
                return [{"title": "No top news found in 'top-news' section.", "link": "#"}]
        else:
            return [{"title": "No 'right-part bg' section found.", "link": "#"}]
    except requests.exceptions.RequestException as e:
        return [{"title": f"Error fetching the URL: {e}", "link": "#"}]


@app.route('/search', methods=['POST'])
def search_news():
    keyword = request.form['keyword'].lower()
    filtered_news = [news for news in scrape_latest_news and scrape_top_news if keyword in news["title"].lower()]
    return render_template('index.html', top_news=filtered_news)

if __name__ == '__main__':
    app.run(debug=True)
