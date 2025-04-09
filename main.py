import requests 
from bs4 import BeautifulSoup
import time


urls = [
    "https://search.brave.com/search?q=Tesla+Stock+Price&source=web",
    "https://search.brave.com/search?q=Ford+Stock+Price&source=web",
    "https://search.brave.com/search?q=Nvidia+Stock+Price&source=web",
    "https://search.brave.com/search?q=AMD+Stock+Price&source=web",
    "https://search.brave.com/search?q=Intel+Stock+Price&source=webe",
]
i = 0
headers={"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:124.0) Gecko/20100101 Firefox/124.0"}
def getprice(i):
       for i in range(len(urls)):
        HTML = requests.get(urls[i], headers=headers)
        soup = BeautifulSoup(HTML.text, "lxml")
        text = soup.find("h1", attrs={"class": "desktop-default-regular t-secondary svelte-37ljbo"}).text + " | " + soup.find("h1", attrs={"class": "desktop-heading-h2 mr-10 t-primary mb-0"}).text
        i = i + 1
        text2 = text
        print(text2)
        continue
        

if __name__ == "__main__":
    while True:
        stock_price = getprice(i)
        print(stock_price)
        time.sleep(60)
