import easygui as eg



if __name__ == '__main__':
	# eg.msgbox('Hello World')

	msg = 'What is your favorite flavor?'
	title = 'Ice Cream Survey'
	choices = ['Vanilla', 'Chocolate', 'Strawberry', 'Rocky Road']
	choice = eg.choicebox(msg, title, choices)

	eg.msgbox('You chose... ' + str(choice))

	if choice == 'Rocky Road':
		eg.msgbox('Yes, Rocky Road is the best')