# -*- coding: utf-8 -*-
import sys
import urllib2
from bs4 import BeautifulSoup
import random

def genRandomStr(strLen):
	newstr = ''
	for i in range(strLen):
		if random.random()<0.5:
			random_char = chr(int(97+26*random.random()))
		else:
			random_char = chr(int(65+26*random.random()))
		newstr = newstr + random_char
	return newstr

def genRandomText(old_text):
	list_str = old_text.split(' ')
	new_text = ''
	for s in list_str:
		new_text = new_text + ' ' + genRandomStr(len(s))
	return new_text[1:]

def processTag(soup, tag_name):
	if tag_name == 'all_tags':
		tags = soup.find_all()
	else:
		tags = soup.find_all(tag_name)
	for e in tags:
		if unicode(e.string) == 'None':
			continue
		newstr = genRandomText(e.string)
		e.string.replace_with(newstr)

if __name__ == 'a__main__':
	filename = u'Electronics, Cars, Fashion, Collectibles, Coupons and More Online Shopping _ eBay.htm'
	html_doc = open('stimulus/'+filename).read()
	soup = BeautifulSoup(html_doc, 'lxml')
	for e in soup.find_all():
		if unicode(e.string) == 'None':
			for s in e.strings:
				print(repr(s))
				#newstr = genRandomText(e.string)
				#s.replace_with('hamasile')
			continue
		newstr = genRandomText(e.string)
		e.string.replace_with(newstr)
	out_htm = str(soup)
	outfile = open('stimulus/out.htm','w')
	outfile.write(out_htm)
	outfile.close()

if __name__ == '__main__':
	filename = u'Electronics, Cars, Fashion, Collectibles, Coupons and More Online Shopping _ eBay.htm'
	html_doc = open('stimulus/'+filename).read()
	soup = BeautifulSoup(html_doc, 'lxml')
	
	processTag(soup, 'all_tags')
	#processTag(soup, 'a')
	#processTag(soup, 'p')
	#processTag(soup, 'span')
	#processTag(soup, 'div')
	
	out_htm = str(soup)
	outfile = open('stimulus/out.htm','w')
	outfile.write(out_htm)
	outfile.close()