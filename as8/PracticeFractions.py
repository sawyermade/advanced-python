import easygui as eg, re, operator, random
from fractions import Fraction

#clears whitespace from a string
def clear_whitespace(s):
    p = re.compile(r'\s')
    return p.sub('', s)

#checks that fraction expr is valid and returns a list of its parts
def regCheck(s):
	regex = r'^(-?[0-9]+)(/[1-9][0-9]*)?([+\-*])(-?[0-9]+)(/[1-9][0-9]*)?$'
	p = re.compile(regex)
	cldws = clear_whitespace(s)

	if p.match(cldws):
		l = p.findall(cldws)
		return l[0]
	else:
		return None

#creates list with [Fraction1, operator, Fraction2]
def createFraction(fracexpr):
	
	frac1expr = fracexpr[0] + fracexpr[1]
	opexpr = fracexpr[2]
	frac2expr = fracexpr[3] + fracexpr[4]

	frac1 = Fraction(frac1expr)
	frac2 = Fraction(frac2expr)
	return [frac1, opexpr, frac2]

#does fraction math depending on opexpr, returns fraction type
def fracMath(fraclist):
	frac1 = fraclist[0]
	op = fraclist[1]
	frac2 = fraclist[2]
	opfunc = {'+':operator.add, '-':operator.sub, '*':operator.mul}

	return opfunc[op](frac1, frac2)

#solver shit
def solver():
	flag = True
	while flag:
		
		#gets fraction expression
		fracstr = eg.enterbox('Enter Fraction Expression', 'Solver Enter Fraction')
		if fracstr == None:
			return None
		fracexprs = regCheck(fracstr)

		#runs if entered expr is valid, spits out answer
		if fracexprs is not None :
			fraclist = createFraction(fracexprs)
			fracresult = fracMath(fraclist)
			question = str(fraclist[0]) + ' ' + fraclist[1] + ' ' + str(fraclist[2]) + ' = '
			answer = str(fracresult)
			choices = ['Solve Another', 'Return']
			choice = eg.buttonbox(question + answer, 'Solver Result', choices)
			if choice == 'Return':
				flag = False

		#shows invalid fraction error, asks if they want to continue or return
		else:
			choices = ['Try Again', 'Return']
			choice = eg.buttonbox('You Have Entered An Invalid Fraction Expression', 'Solver Fraction Error', choices)
			if choice == 'Return':
				flag = False

#reg check for quizzer answer
def regCheckAnswer(s):
	regex = r'^(-?[0-9]+)(/[1-9][0-9]*)?$'
	p = re.compile(regex)
	cldws = clear_whitespace(s)

	if p.match(cldws):
		return True
	else:
		return False

#quizzer shit
def quizzer():
	flag = True
	opfunc = {'+':operator.add, '-':operator.sub, '*':operator.mul}
	while flag:
		#gets op and creates problem and answer
		op = eg.buttonbox('Please Choose An Operator', 'Quizzer Operator Select', ['+', '-', '*', 'Return'])
		if op == 'Return':
			break
		num1 = random.randint(-15, 15)
		num2 = random.randint(-15, 15)
		den1 = random.randint(1, 15)
		den2 = random.randint(1, 15)
		f1 = Fraction(num1, den1)
		f2 = Fraction(num2, den2)
		result = opfunc[op](f1, f2)

		#creates question and asks for answer
		question = str(f1) + ' ' + op + ' ' + str(f2) + ' = '
		answer = eg.enterbox(question, 'Quizzer Question')

		#if user hit cancel, returns to operator select
		if answer == None:
			continue

		#loops until they enter a proper fraction answer or hits cancel
		ansRegCheck = regCheckAnswer(answer)
		while not ansRegCheck:
			eg.buttonbox('You Did Not Enter A Valid Fraction Expression', 'Error Invalid Fraction', ['OK'])
			answer = eg.enterbox(question, 'Quizzer Question')
			if answer == None:
				break
			ansRegCheck = regCheckAnswer(answer)

		#checks if they hit cancel again
		if answer == None:
			continue

		#clears white space from answer
		answer = clear_whitespace(answer)

		#prints result window. correct, partially correct not reduced, wrong
		if answer == str(result):
			choice = eg.buttonbox('Congradulations, Your Answer Was Correct!', 'Quizzer Results', ['Another Quiz', 'Return'])
			if choice == 'Return':
				flag = False

		elif str(Fraction(answer)) == str(result):
			choice = eg.buttonbox('Your Answer Was Correct But Not Reduced\nCorrect Answer: {0}{1}'.format(question, str(result)), 'Quizzer Results', ['Another Quiz', 'Return'])
			if choice == 'Return':
				flag = False

		else:
			choice = eg.buttonbox('Your Answer Was Not Correct :(\nCorrect Answer: {0}{1}'.format(question, str(result)), 'Quizzer Results', ['Another Quiz', 'Return'])
			if choice == 'Return':
				flag = False

#main shit
if __name__ == '__main__':
	
	#sets up main buttonbox stuff
	msgIntro = 'Welcome To Practice Fractions'
	titleIntro = 'Practice Fractions'
	choicesIntro = ['Solver', 'Quizzer', 'Quit']
	flag = True

	#runs until they select quit
	while flag:
		choiceIntro = eg.buttonbox(msgIntro, titleIntro, choicesIntro)
		
		if choiceIntro == 'Quit':
			flag = False

		if choiceIntro == 'Solver':
			solver()

		if choiceIntro == 'Quizzer':
			quizzer()

	# #testing shit
	# f1 = Fraction('3/4')
	# print(f1)
	# f1 = Fraction(-3, 2)
	# print(f1)
	# f1 = Fraction('10')
	# print(f1)

	# f1 = Fraction('10')
	# f2 = Fraction('-5/2')
	# f3 = operator.add(f1, f2)
	# print(f3)

	# s1 = '3/4 + 5/4'
	# regCheck(s1)
	# s2 = '3/4 + 5'
	# regCheck(s2)
	# # s3 = '3/0 + 5'
	# # regCheck(s3)
	# s4 = '5 + 5/4'
	# fracexpr1 = regCheck(s4)
	# print(fracexpr1)
	# fracexpr2 = regCheck(s1)
	# print(fracexpr2)

	# f1list = createFraction(fracexpr1)
	# print(f1list)
	# f1 = fracMath(f1list)
	# print(f1)