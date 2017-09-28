'''
Daniel Sawyer Assignment 1 Collatz Fall 2017
'''
def collatz_sequence():
	#try and except to make sure input is integer
	try:
		n = int(input('Enter number: '))

	# except Exception as e:
	except ValueError:
		#print(e)
		print('Invalid input: must be an integer')
		return False
	print()
	
	#if user enter 1, outputs 1 and returns true
	if n == 1:
		print(n)
		return True
	
	#loop collatz until it reaches 1
	while n > 1:
		n = collatz(n)
	return True

def collatz(number):
	if number % 2 == 0:
		print(number//2)
		return number//2
	else:
		print(3*number+1)
		return 3*number+1

# if __name__ == "__main__":
# 	collatz_sequence()
# 	exit()
collatz_sequence()
exit()