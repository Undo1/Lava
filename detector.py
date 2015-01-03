import re
import random
import requests
import mechanize
import sys
import urllib
from BeautifulSoup import BeautifulSoup

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)
br.addheaders = [('User-agent', 'Firefox')]

url = 'http://api.stackexchange.com/2.2/answers?pagesize=3&order=desc&sort=activity&site=stackoverflow&filter=!)Q2AgVryMp_tSg8sztC*RY8i'

response = requests.get(url).json()

items = response["items"]

for item in items:
	try:
		p=re.compile("([\w*\s]{50,})")
		body = random.choice(p.search(item["body"]).groups())
	except:
		continue

	print "---------"
	print "-- Searching for: " + body
	print "-- Source answer: " + item["link"]
	print "---------"

	html = br.open('https://www.google.com/search?q="' + urllib.quote(body) + '"').read()

	soup = BeautifulSoup(html)

	if "No results found for" in soup.text:
		print "-- No Results Found"
		continue

	cites = soup.findAll('cite')

	p=re.compile("\/url\?q=(.*)&sa")

	for elem in cites:
		try:
			print p.search(elem.parent.parent.parent.find('h3').find('a').get('href')).groups()[0]
		except:
			continue
