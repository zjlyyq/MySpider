from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
# filter out live ids from a url
def filterLiveIds(url):
     html = urlopen(url)
     liveIds = set()
     bsObj = BeautifulSoup(html, "html.parser")
     for link in bsObj.findAll("a", href=re.compile("^(/l/)")):
         if 'href' in link.attrs:
             newPage = link.attrs['href']
             liveId = re.findall("[0-9]+", newPage)
             liveIds.add(liveId[0])
     return liveIds

url='http://www.huajiao.com/category/1000'
liveIds = filterLiveIds(url)
print(liveIds)