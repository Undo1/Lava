import re
import mechanize
import sys
import urllib
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False) 
br.addheaders = [('User-agent', 'Firefox')]

print "---------"
print "-- Searching for: " + sys.argv[1]
print "---------"

html = br.open('https://www.google.com/search?q="' + urllib.quote(sys.argv[1]) + '"').read()

soup = BeautifulSoup(html)

if "No results found for" in soup.text:
	print "-- No Results Found"
	sys.exit("")

cites = soup.findAll('cite')

p=re.compile("\/url\?q=(.*)&sa")

for elem in cites:
	try:
		print p.search(elem.parent.parent.parent.find('h3').find('a').get('href')).groups()[0]
	except AttributeError:
		print "meh"
