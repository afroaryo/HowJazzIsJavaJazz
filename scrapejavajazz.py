from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

url = 'https://en.wikipedia.org/wiki/Jakarta_International_Java_Jazz_Festival'

uClient = uReq(url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

international = page_soup.findAll("div",{"class":"div-col columns column-width"})

filename = "artists.csv"
f = open(filename,"w")

headers = "artists\n"
f.write(headers)


for intern in international:
    hai = intern.text
    print(hai)
    f.write(hai + "\n")

f.close()