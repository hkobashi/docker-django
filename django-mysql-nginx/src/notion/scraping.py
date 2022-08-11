import requests
import feedparser
import pprint
import bs4

# r = requests.get("https://weather.tsukumijima.net/api/forecast/city/170020")

# length = len(r.json()["forecasts"])

# for i in range(0, length):
#   print(r.json()["forecasts"][i]["date"])
#   print(r.json()["forecasts"][i]["telop"])
#   print(r.json()["forecasts"][i]["temperature"]["max"]["celsius"])

# data = feedparser.parse("https://news.yahoo.co.jp/rss/topics/domestic.xml")
# num = len(data["entries"])
# for i in range(0, num):
#   print(data["entries"][i]["title"])
#   print(data["entries"][i]["published"])
#   print(data["entries"][i]["link"])

r = requests.get("https://www.oreilly.co.jp/ebook/")
soup = bs4.BeautifulSoup(r.text, "html.parser")

#print(soup)

table = soup.find("table")
#print(table.prettify())

release_book = table.findAll("a")
for i in release_book:
  print(i.text)