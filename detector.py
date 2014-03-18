import re
import mechanize
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False) 
br.addheaders = [('User-agent', 'Firefox')]

html = br.open('https://www.google.com/search?q="this+is+a+pancake"').read()

soup = BeautifulSoup(html)

cites = soup.findAll('cite')

for elem in cites:
	print elem.text