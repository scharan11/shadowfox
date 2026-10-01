import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    books = soup.find_all("h3")

    print("Book Titles:")
    print()

    for book in books:
        title = book.find("a")["title"]
        print(title)

else:
    print("Failed to access the website.")
    print("Status code:", response.status_code)
