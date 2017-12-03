import re

expr1 = r'[\d{3}\-|(\d{3})]?\d{3}-\d{4}'

expr2 = r'(?:\d{3}-|\(\d{3}\))?(?:\d{3}-\d{4})'

reg = re.compile(expr2)
print(reg.match('613-3984'))
print(reg.match('813-613-3984'))
print(reg.match('(813)613-3984'))

temp = r'[\d\d\d\-]?\d'
reg2 = re.compile(temp)
print(reg2.match('3'))