# scraper.py

import requests
from bs4 import BeautifulSoup

def scrape_headlines():
    url = input("Enter the URL of the news website to scrape headlines from (default: BBC News): ")
    if not url:
        url = "https://www.bbc.com/news"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch the webpage.")
        return

    soup = BeautifulSoup(response.text, "html.parser")

    # Most BBC headlines appear under <h2> tags
    headlines = soup.find_all("h2")

    cleaned_headlines = []

    for h in headlines:
        text = h.get_text(strip=True)
        if text and len(text) > 5:   # Avoid empty or junk lines
            cleaned_headlines.append(text)

    # Save to a text file
    with open("headlines.txt", "w", encoding="utf-8") as f:
        for line in cleaned_headlines:
            f.write ("----------------------------------\n")
            f.write(line + "\n")
        f.write ("----------------------------------\n")
        
    print(f"Scraping completed! {len(cleaned_headlines)} headlines saved to headlines.txt")


if __name__ == "__main__":
    scrape_headlines()
