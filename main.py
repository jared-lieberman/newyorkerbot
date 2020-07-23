import pandas as pd
from bs4 import BeautifulSoup
import requests

from urllib.request import urlopen, Request
import re






def get_page_captions(reg_url):

	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
	req = Request(url=reg_url, headers=headers) 
	html = urlopen(req).read() 

	soup = BeautifulSoup(html, "html.parser")
	#print(soup.text)

	match = re.findall('Winning caption:(.+?)”', soup.text, flags=re.IGNORECASE)

	print(match)
	print(len(match))

	return(match)




def scrape_captions():
	
	#https://micromismanagement.com/tag/new-yorker/page/2/

	#page_num = 1
	
	#reg_url = "https://micromismanagement.com/tag/new-yorker/page/1/"
	#captions_list = get_page_captions(reg_url)

	for i in range(10):
		#print(i)
		reg_url =  "https://micromismanagement.com/tag/new-yorker/page/" + str(i + 1) + "/"
		if i + 1 == 1: captions_list = get_page_captions(reg_url)
		else: captions_list.extend(get_page_captions(reg_url))

	print(len(captions_list))
	print(captions_list)






def main():
	scrape_captions()




if __name__ == "__main__":
    main()