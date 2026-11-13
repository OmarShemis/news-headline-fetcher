import os
import requests

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
country = input("Enter country code (exemple: us, jp, eg): ")
category = input("Enter category code (exemple: technology, sports, business): ")

url = "https://newsapi.org/v2/top-headlines"

params = {
    "apikey": api_key,
    "country": country,
    "category": category,
    "pagesize": 10
}

response = requests.get(url, params=params)
data = response.json()

if response.status_code == 200:
    articles = data["articles"]

    if not articles:
        print("No articles found.")
    else:
        for index, article in enumerate(articles):
            print(f"{index + 1}. {article['title']}")
            print(f"   {article['url']}\n")
else:
    print("error:", data.get("message", "could not fetch news."))
