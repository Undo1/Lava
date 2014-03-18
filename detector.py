import re
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False) 
br.addheaders = [('User-agent', 'Firefox')]

print br.open("https://www.google.com/search?q=this+is+a+test").read()