import requests
from bs4 import BeautifulSoup

def scrape(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string.strip() if soup.title else "No Title"
    book_titles = [h5.get_text(strip=True) for h5 in soup.select('h5')]
    img_urls = [img.get("src") for img in soup.find_all("img") if img.get("src")]
    print("Page Title:", title)
    print("\nBook Titles:")
    for i, title in enumerate(book_titles, 1):
        print(f"  {i}. {title}")
        
    print("\nImage Links:")
    for img_url in img_urls:
        print("  ", img_url)


url = "https://www.iranketab.ir/tag/1821-hot-books"
scrape(url)
