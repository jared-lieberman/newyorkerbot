import pandas as pd
from bs4 import BeautifulSoup
import requests

from urllib.request import urlopen, Request








def scrape_captions():
	

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	reg_url = "https://micromismanagement.com/tag/new-yorker/"
	req = Request(url=reg_url, headers=headers) 
	html = urlopen(req).read() 
	print(html)

	#url = "https://micromismanagement.com/tag/new-yorker/"
	#req = requests.get(url)

	#print(req)

	#soup = BeautifulSoup(req.text, "html.parser")
	#print(type(soup.string))

	#print(soup.title)




def main():
	scrape_captions()




if __name__ == "__main__":
    main()