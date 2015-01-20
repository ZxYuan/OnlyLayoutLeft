# -*- coding: utf-8 -*-
import sys
import os
import cStringIO, urllib2
from PIL import Image

prefix = u'Trending stories on Indian Lifestyle, Culture, Relationships, Food, Travel, Entertainment, News & New Technology News - Indiatimes.com'
directory_name = u'stimulus/'+prefix+u'_files/'

print 'Generating images...'
pngnames = []
for f in os.listdir(directory_name):
	if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.gif') :
		pngnames.append(f)
for pname in pngnames:
	print directory_name+pname
	im = Image.open(directory_name+pname)
	url = 'http://localhost:8080/'+str(im.size[0])+'x'+str(im.size[1])
	f = urllib2.urlopen(url) 
	data = f.read()
	with open(directory_name+pname, "wb") as img:
		img.write(data)
print 'Done!'