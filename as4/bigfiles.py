'''
Daniel Sawyer Assignment 4 bigfiles Fall 2017
'''
import os

def bigfiles(basepth):
	# file size we are looking for and file list
	minfsize = 104857600
	flist = []

	# goes through all dir and files and finds files >= minfilesize
	# then returns a list of those files
	for root, dirs, files in os.walk(basepth):
		for name in files:
			if root.endswith('/'):
				fpath = root + name
			else:
				fpath = root + '/' + name
			fsize = os.path.getsize(fpath)
			if fsize >= minfsize:
				flist.append(fpath)
	return flist

# main funtion to test it out, i had a temp dir in the same dir as bigfiles.py
flist = bigfiles('temp')
for name in flist:
	print(name)