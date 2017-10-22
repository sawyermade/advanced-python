def q1():
	D = {}
	S = 'one'
	L = ['one', 'two']
	T = ('one', 'two')

	D[S] = 'bacon'
	D[T] = 'bacon'
	#D[L] = 'bacon'
	D[5] = 'bacon'

	print(D)
	print(D[('one', 'two')])

def func1(L):
	L[0] = 5
def func2(L):
	L = L[:-1] + [10]

def reverseString():
	
	S = input('Enter a sentence: ')

	S = S.split(' ')
	# temp = []

	# for x in S:
	# 	temp = [x] + temp
	S.reverse()
	S = ' '.join(S)
	
	print(S)

def half_backwards(L):
	# half = len(L) // 2
	# right = L[:half]
	# left = L[half:]
	# L = left + right
	# print(L)
	# return L
	return L[len(L)//2:] + L[:len(L)//2]
def favFood():

	nameFood = {}

	x = input('Name: ')
	while x:
		y = input('Food: ')
		if x not in nameFood:
			nameFood[x] = [y]
		else:
			#nameFood[x] += [y]
			nameFood[x].append(y)
		print()
		x = input('Name: ')

	for i, j in nameFood.items():
		print(i + ' likes', end=' ')
		
		if len(nameFood[i]) == 1:
			print(nameFood[i][0])

		if len(nameFood[i]) == 2:
			print(nameFood[i][0] + ' and ' + nameFood[i][1])

		else:
			for k in j[:-1]:
				print(k, end=', ')
			print('and ' + j[-1])

def getInts(fname):
	f = None

	try:
		f = open(fname)
		return [int(x) for x in f.read().split()]
	except FileNotFoundError as e1:
		print(e1)
	except TypeError as e2:
		print(e2)
	except ValueError as e3:
		print(e3)
	finally:
		if f:
			f.close()

def arbSum(*arg):
	return sum(arg)/len(arg)

# print('q1 shit')
# q1()

# K = [3,6,5,2]
# func1(K)
# print(K)
# J = [8,4,9,1,6]
# func2(J)
# print(J)
# F = J[:]
# print(F)
# print(J)

# reverseString()

# L = [1, 2, 3, 4, 5, 6, 7]
# print(half_backwards(L))

# favFood()

# n = 20
# OddsSquared = [x**2 for x in range(1, n) if x%2]
# print(OddsSquared)

# print(getInts('temp.txt'))

# K = [8, 2, 3, 8, 2, 6, 3, 69, 69, 72]
# L = list(set(K))
# print(L)
# L.sort(key=K.index)
# print(L)

# L1 = []
# L2 = [1, 0]
# L3 = [2, 3]
# print(L1 and L2)
# print(L1 or L2)
# print(L2 and L3)
# print(L3 and L2)
# print(L2 and L1)
# print(~L1)

# print(arbSum(1, 2, 3, 4, 5))

L = [(1.0, 3.2), (-1.0, 1.0), (1.0,1.0)]
L.sort(key=sum)
print(L)

print('%s can go eat %d potatoes for $%f each' % ('daniel', 100, 1.75))
print('{0} can go eat {1} potatoes for ${2} each'.format('daniel', 100, 1.75))