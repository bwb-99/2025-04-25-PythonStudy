import urllib.request as req
from bs4 import BeautifulSoup
from urllib import parse
import json
url="https://www.kobis.or.kr/kobis/business/main/searchMainDailyBoxOffice.do"
text_data=req.urlopen(url).read().decode("UTF-8")
print(text_data)