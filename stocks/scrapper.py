from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request as req
import csv

my_url = 'https://in.investing.com/indices/s-p-bse-500-components'
request = req(my_url, headers={'User-Agent': 'Mozilla/5.0'})
uClient = uReq(request)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')

table = page_soup.find("table")
headers = [th.text for th in table.select("tr th")]

with open("/Users/sourabh/Documents/out.csv", "w") as f:
    wr = csv.writer(f)
    wr.writerow([headers[i] for i in range(1, 6)])
    for row in table.select("tr + tr"):
        print(len(row.find_all("td")))
        wr.writerows([[row.find_all("td")[i].text for i in range(1, 6)]])
