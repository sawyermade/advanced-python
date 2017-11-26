import pickle

class Transaction(object):
	
	'''
	>>> T = Transaction(99, '11-20-17')
	
	>>> print(T.amount)
	99
	
	>>> print(T.date)
	11-20-17
	
	>>> print(T.currency)
	USD
	
	>>> print(T.usd_conversion_rate)
	1
	
	>>> print(T.description)
	None

	>>> print(T.usd)
	99
	
	>>> T.amount = 69
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute
	
	>>> T.date = '11-11-11'
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute
	
	>>> T.currency = 'CAD'
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute

	>>> T.usd = 100
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute

	>>> T.usd_conversion_rate = 2
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute
	'''

	def __init__(self, amount, date, currency='USD', usd_conversion_rate=1, description=None):
		self.__amount = amount
		self.__date = date
		self.__currency = currency
		self.__usd_conversion_rate = usd_conversion_rate
		self.__description = description
		self.__usd = self.__amount * self.__usd_conversion_rate

	@property
	def amount(self):
		return self.__amount

	@property
	def date(self):
		return self.__date

	@property
	def currency(self):
		return self.__currency

	@property
	def usd_conversion_rate(self):
		return self.__usd_conversion_rate

	@property
	def description(self):
		return self.__description

	@property
	def usd(self):
		return self.__usd
	

class Account(object):
	
	'''
	>>> trans = Transaction(99, 11-20-17)

	>>> translist = [Transaction(100, 11-21-17), Transaction(200, 11-22-17), Transaction(300, 11-23-17, 'USD')]

	>>> ac1 = Account(123, 'dan', translist)
	Traceback (most recent call last):
		...
	ValueError: Account name must be at least 4 characters long.

	>>> ac1 = Account(123, 'daniel', translist)

	>>> print(ac1.account_name)
	daniel
	
	>>> print(len(ac1))
	3

	>>> print(ac1.balance)
	600

	>>> print(ac1.all_usd)
	True

	>>> ac1.apply(trans)

	>>> print(len(ac1))
	4

	>>> ac1.save()

	>>> trans2 = Transaction(69, 6-1-84)

	>>> ac1.apply(trans2)

	>>> print(len(ac1))
	5

	>>> ac1.load()

	>>> print(len(ac1))
	4

	>>> ac2 = Account(321, 'robby', translist)

	>>> ac2.load(123)
	Cannot load 123.acc, account numbers do not match

	>>> ac2.account_name = 'robby new'

	>>> ac2.account_name = 'rob'
	Traceback (most recent call last):
		...
	ValueError: Account name must be at least 4 characters long.

	>>> ac2.account_number = 69
	Traceback (most recent call last):
		...
	AttributeError: can't set attribute
	'''

	def __init__(self, account_number, account_name, transactions):
		self.__account_number = account_number
		self.account_name = account_name
		self.__transactions = transactions

	def __len__(self):
		return len(self.__transactions)

	@property
	def account_number(self):
		return self.__account_number

	@property
	def account_name(self):
		return self.__account_name

	@account_name.setter
	def account_name(self, account_name):
		if len(account_name) < 4:
			raise ValueError('Account name must be at least 4 characters long.')
		else:
			self.__account_name = account_name

	@property
	def balance(self):
		sum = 0
		for x in self.__transactions:
			sum += x.usd
		return sum

	@property
	def all_usd(self):
		for x in self.__transactions:
			if x.currency is not 'USD':
				return False	
		return True

	def apply(self, trans):
		self.__transactions.append(trans)

	def save(self):
		fh = None
		try:
			data = [self.__account_number, self.__account_name, self.__transactions]
			name = str(self.__account_number) + '.acc'
			fh = open(name, 'wb')
			pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)
		except (EnvironmentError, pickle.PicklingError) as e:
			raise SaveError(str(e))
		finally:
			if fh is not None:
				fh.close()

	def load(self, anum=None):
		fh = None
		name = None
		if anum is not None:
			name = str(anum) + '.acc'
		else:
			name = str(self.__account_number) + '.acc'
		try:
			fh = open(name, 'rb')
			data = pickle.load(fh)
			if data[0] is not self.__account_number:
				return print('Cannot load {0}, account numbers do not match'.format(name))
			self.__account_name = data[1]
			self.__transactions = data[2]
		except (EnvironmentError, pickle.UnpicklingError) as e:
			raise LoadError(str(e))
		finally:
			if fh is not None:
				fh.close()
			

if __name__ == '__main__':
	import doctest
	doctest.testmod()