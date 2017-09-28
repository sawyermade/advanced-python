'''
Daniel Sawyer Assignment 4 bigfiles Fall 2017
'''
import os

def bigfiles(basepth):

	maxfsize = 104857600
	flist = []

	for root, dirs, files in os.walk(basepth):
		for name in files:
			if root == basepth:
				fpath = root + name
			else:
				fpath = root + '/' + name
			fsize = os.path.getsize(fpath)
			if fsize >= maxfsize:
				flist.append(fpath)
	return flist

flist = bigfiles('temp/')
for name in flist:
	print(name)