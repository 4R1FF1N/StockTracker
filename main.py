import requests 
from bs4 import BeautifulSoup
import time


urls = [
    "https://www.google.com/search?q=tesla+stock+price",
    "https://www.google.com/search?q=nvidia+stock+price",
    "https://www.google.com/search?q=apple+stock+price",
    "https://www.google.com/search?q=cisco+stock+price",
    "https://www.google.com/search?q=microstrategy+stock+price",
]
i = 0
headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"}
def getprice(i):
       for i in range(len(urls)):
        HTML = requests.get(urls[i], headers=headers)
        soup = BeautifulSoup(HTML.text, "lxml")
        text = soup.find("div", attrs={"class": "PZPZlf ssJ7i B5dxMb"}).text + " | " + soup.find("span", attrs={"jsname": "vWLAgc"}).text + soup.find("span", attrs={"jsname": "T3Us2d"}).text
        i = i + 1
        text2 = text
        print(text2)
        continue
        

if __name__ == "__main__":
    while True:
        stock_price = getprice(i)
        print(stock_price)
        time.sleep(60)
