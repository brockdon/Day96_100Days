import requests
from bs4 import BeautifulSoup

#def changingPage(pageNumber):
  
pageNumber = 2
url =f"https://news.ycombinator.com/?p={pageNumber}"

response = requests.get(url)
html = response.text

soup = BeautifulSoup(html,"html.parser")

Links = soup.find_all("a")

for link in Links:
  link =str(link).lower()
  if "replit" in link:
    if "sitestr" in link:
      pass
    else:
      headline = link.split('"')
      print(headline)
      print(link)
  elif "python" in link:
    if "sitestr" in link:
      pass
    else:
      link_split = link.split('"')
      linkUrl = link_split[1]
      headline = link_split[2]
      print(headline)
      print(linkUrl)
  else:
    pass