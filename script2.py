import bs4
import urllib.request 
from bs4 import BeautifulSoup as soup
import numpy as np
from bs4 import SoupStrainer


class Chord:
	def __init__(self, index = []):
		self.index = index


def scrape():
	#gets page, right now on random tay sway song.
	my_url = 'https://www.e-chords.com/style/country'
	uClient = urllib.request.urlopen(my_url)
	page_html = uClient.read()
	uClient.close()

	#creats page
	strainer = SoupStrainer('p')
	artists = soup(page_html, "lxml", parse_only = strainer)
	for a in artists.find_all('a'):
		my_url = a['href']
		uClient = urllib.request.urlopen(my_url)
		page_html = uClient.read()
		uClient.close()
		strainer = SoupStrainer({"class" :"types"})
		songs = soup(page_html, "lxml", parse_only = strainer)
		print(a)


	#artists = page_soup.findAll('td', {"class" : "alphabet"})
		


def main():
	scrape()


if __name__ == "__main__":
    main()