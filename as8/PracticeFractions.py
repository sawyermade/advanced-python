import easygui as eg, re, operator
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
		# print('{0} is a match'.format(cldws))
		return p.findall(cldws)
	else:
		return None

#creates list with [Fraction1, operator, Fraction2]
def createFraction(fracexpr):
	
	frac1expr = fracexpr[0][0] + fracexpr[0][1]
	opexpr = fracexpr[0][2]
	frac2expr = fracexpr[0][3] + fracexpr[0][4]

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
		fracstr = eg.enterbox()
		fracexprs = regCheck(fracstr)

		if fracexprs is not None:
			fraclist = createFraction(fracexprs)
			fracresult = fracMath(fraclist)
			# print(fracresult)
			choices = ['Solve Another', 'Return']
			choice = eg.buttonbox(str(fracresult), 'Solver Result', choices)
			if choice == 'Return':
				flag = False

		else:
			choices = ['Try Again', 'Return']
			choice = eg.buttonbox('You Have Entered An Invalid Fraction Expression', 'Solver Error', choices)
			if choice == 'Return':
				flag = False

#quizzer shit
def quizzer():
	pass

#main shit
if __name__ == '__main__':
	
	msgIntro = 'Welcome To Practice Fractions'
	titleIntro = 'Practice Fractions'
	choicesIntro = ['Solver', 'Quizzer', 'Quit']
	flag = True

	while flag:
		choiceIntro = eg.buttonbox(msgIntro, titleIntro, choicesIntro)
		#print(choiceIntro)
		if choiceIntro == 'Quit':
			# print('Quitting')
			flag = False

		if choiceIntro == 'Solver':
			solver()

		if choiceIntro == 'Quizzer':
			quizzer()

	#testing shit
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