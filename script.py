import bs4
import pickle
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import numpy as np
from bs4 import SoupStrainer

class Chord:
	def __init__(self, index = []):
		self.index = index


def scrape():
	#gets page, right now on random tay sway song.
	my_url = 'https://www.e-chords.com/style/country'
	uClient = uReq(my_url)
	page_html = uClient.read()
	uClient.close()

	#creats page
	strainer = SoupStrainer('p')
	artists = soup(page_html, "lxml", parse_only = strainer)
	for a in artists.find_all('a'):
		my_url = a['href']
		uClient = uReq(my_url)
		page_html = uClient.read()
		uClient.close()
	
		page_soup = soup(page_html, "html.parser")
		songs = page_soup.findAll('ul', {"id" : "results"})
		for song in songs:
			second = song.findAll('a', {"class" : "ta"})
			for a in second:
				my_url = a['href']
				uClient = uReq(my_url)
				page_html = uClient.read()
				uClient.close()
				page_soup = soup(page_html, "html.parser")
				#now lets find where the chords are
				chords = page_soup.findAll('u')
				#iterates over chords and adds everything to a list
				myList = list()
				for i in chords: 
					myList.append(i.getText())
	#if not i in S CHECKING IF SOMETHIN


def main():
	scrape()


if __name__ == "__main__":
    main()