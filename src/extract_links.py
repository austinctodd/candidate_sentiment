#!/Users/austintodd/anaconda/bin/python

# Load libraries
from BeautifulSoup import BeautifulSoup
import urllib2
import re

# Load web page content as urllib2 object
html_page=urllib2.urlopen('http://www.presidency.ucsb.edu/nomination.php')

# Create Beautiful Soup object from page content
soup=BeautifulSoup(html_page)

# Loop through all the lines that link to speech files - extract speech web address and speaker
speaker=[]
pagelink=[]
for link in soup.findAll('a',attrs={'href': re.compile("^http://www.presidency.ucsb.edu/ws/index")}):
	speaker.append(re.sub(r'\W+',' ',link.string))
	pagelink.append(link.get('href'))

