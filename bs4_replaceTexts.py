# -*- coding: utf-8 -*-
import sys
import urllib2
from bs4 import BeautifulSoup, NavigableString, Comment
import random

HAMA = True # whether work on the case of multi child nodes

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

def processTag_text(tags):
	for e in tags:
		if isinstance(e, Comment): # exclude comments
			continue
		if HAMA and unicode(e.string) == 'None': # for the case of multi child nodes
			chlds = e.contents
			for c in chlds:
				if isinstance(c, Comment): # exclude comments
					continue
				if isinstance(c, NavigableString):
					if c == '\n':  # exclude \n
						continue
					newstr = genRandomText(c.string)
					c.string.replace_with(newstr)	
			continue
		newstr = genRandomText(e.string)
		e.string.replace_with(newstr)

def processTag_input(tags):
	for e in tags:
		if e.get('value'):
			e['value'] = genRandomText(e['value'])
		if e.get('placeholder'):
			e['placeholder'] = genRandomText(e['placeholder'])

def processTag(soup, tag_name):
	if tag_name == 'all_tags':
		tags = soup.find_all()
		processTag_text(tags)
	elif tag_name == 'input':
		tags = soup.find_all('input')
		processTag_input(tags)
	else:
		tags = soup.findAll(tag_name)
		processTag_text(tags)

if __name__ == '__main__':
	filename = u'Electronics, Cars, Fashion, Collectibles, Coupons and More Online Shopping _ eBay.htm'
	html_doc = open('stimulus/'+filename).read()
	soup = BeautifulSoup(html_doc, 'lxml')
	
	#processTag(soup, 'all_tags')
	processTag(soup, 'a')
	processTag(soup, 'p')
	processTag(soup, 'input')
	processTag(soup, 'span')
	processTag(soup, 'div')
	processTag(soup, 'h2')
	
	out_htm = str(soup)
	outfile = open('stimulus/out.htm','w')
	outfile.write(out_htm)
	outfile.close()