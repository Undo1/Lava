import requests
import sys
import random
import re

url = 'http://api.stackexchange.com/2.2/answers?pagesize=1&order=desc&sort=activity&site=stackoverflow&filter=!)Q2AgVryMp_tSg8sztC*RY8i'

response = requests.get(url).json()

test = response["items"][0]["body"]

try:
	p=re.compile("([\w*\s]{50,})")
	print random.choice(p.search(test).groups())
except:
	sys.exit()	
