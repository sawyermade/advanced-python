'''
Daniel Sawyer Assignment 3 madlibs Fall 2017
'''
def mad_libs(inputname, outputname):

	#opens input and output files
	try:
		ifile = open(inputname)
		ofile = open(outputname, 'w')
	except Exception as e:
		print(e)
		return

	#copies orignal strings to og, then splits to word_list
	og = ifile.read()
	word_list = og.split()

	#gets word_list length and punctuation to ignore
	list_length = len(word_list)
	punc = '!,.?:;'

	#loop that goes through all the words
	for x in range(0,list_length):
		
		#changes any of 4 keywords with user input
		if word_list[x].strip(punc) == 'ADJECTIVE':
			word_list[x] = word_list[x].replace('ADJECTIVE', input('Enter an adjective: '))
		
		elif word_list[x].strip(punc) == 'NOUN':
			word_list[x] = word_list[x].replace('NOUN', input('Enter a noun: '))

		elif word_list[x].strip(punc) == 'ADVERB':
			word_list[x] = word_list[x].replace('ADVERB', input('Enter an adverb: '))

		elif word_list[x].strip(punc) == 'VERB':
			word_list[x] = word_list[x].replace('VERB', input('Enter a verb: '))

		#writes to output file
		if(x == list_length-1):
			ofile.write(word_list[x])
		else:
			ofile.write(word_list[x] + ' ')

	#closes input and output
	ifile.close()
	ofile.close()

#main function stuff
#if __name__ == '__main__':
mad_libs('input.txt', 'output.txt')
exit()
