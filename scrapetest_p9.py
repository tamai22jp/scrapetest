from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
#bsObj = BeautifulSoup(html.read())
#beautifulsoup 4.4.0 たぶん　でエラーなので、下記へ
bsObj = BeautifulSoup(html.read(), "html.parser")

print(bsObj.h1)