'''
Daniel Sawyer Assignment 3 tableprinter Fall 2017
'''
def printTable(L):
	#if list is empty, prints newlinle and returns
	if not L:
		print()
		return

	#vars used
	numLists = len(L)
	numItems = len(L[0])
	biggest = -1
	colsizes = []

	#finds max column sizes
	for x in range(0, numLists):
		biggest = -1
		for y in range(0, numItems):
			biggest = max(biggest, len(L[x][y]))
		colsizes.append(biggest)

	#prints lists using rjust
	for y in range(0, numItems):
		for x in range(0, numLists):
			if x < numLists-1:
				print(L[x][y].rjust(colsizes[x]), end=' ')
			else:
				print(L[x][y].rjust(colsizes[x]), end='\n')

#main function stuff
#if __name__ == '__main__':
tableData = [['apples', 'oranges', 'cherries', 'banana'],
			 ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
testList = []
printTable(testList)
exit()