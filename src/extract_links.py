#!/Users/austintodd/anaconda/bin/python

# Load libraries
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import nltk

# Load web page content as urllib2 object
html_page=urllib2.urlopen('http://www.presidency.ucsb.edu/nomination.php')

# Create Beautiful Soup object from page content
soup=BeautifulSoup(html_page)

# Loop through all the lines that link to speech files - extract speech web address and speaker
speakers=[]
speeches=[]
for link in soup.findAll('a',attrs={'href': re.compile("^http://www.presidency.ucsb.edu/ws/index")}):
	speakers.append(re.sub(r'\W+',' ',link.string))

    # Open new Beautifulsoup object with contained link
    soup2=BeautifulSoup(urllib2.urlopen(link.get('href')))
    
    # Initialize string that will contain transcript
    speech=''

    # Extract transcript - first find all <p> references
    for s in soup2.findAll('p'):
        
        # Not all <p> instances created equal
        # May miss some content if the paragraph has a formatting object
        #     e.g. <i>The President.</i>
        #          <i>Audience Members</i>
        #          <i>Laughter</i>
        #          <i>applause</i>
        #          <i>laughter and applause</i>
        if s.i:
            if any(b in s.i.text.lower() for b in ['laughter','president','applause']):
                s.i.decompose()
                speech=speech+s.text+' '
        else:
            speech=speech+s.text+' '

    speeches.append(speech)


