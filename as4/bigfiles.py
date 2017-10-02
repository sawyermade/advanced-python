'''
Daniel Sawyer Assignment 4 bigfiles Fall 2017
'''
import os

def bigfiles(basepth):
	
	#file size we are looking for and file list
	# minfsize = 100000000 #1000^2 * 100
	minfsize = 104857600 #1024^2 * 100
	flist = []

	#goes through all dir and files and finds files >= minfilesize
	for root, dirs, files in os.walk(basepth):
		for name in files:
			fpath = os.path.join(root, name)
			if os.path.getsize(fpath) > minfsize:
				flist.append(fpath)
	
	#returns list of files >= minfsize
	return flist

#main funtion to test it out, i had a temp dir in the same dir as bigfiles.py
flist = bigfiles('temp/')
for name in flist:
	print(name)