import re
# if you need any other imports, put them below


class BadPasswordCharacter(Exception):
    pass

class InvalidFractionExpression(Exception):
    pass

def strong_pwd(pwd_string):
    restr = r'^(?=[a-zA-Z0-9]*[a-z][a-zA-Z0-9]*)(?=[a-zA-Z0-9]*[A-Z][a-zA-Z0-9]*)(?=[a-zA-Z0-9]*[0-9][a-zA-Z0-9]*)[a-zA-Z0-9]{8,}$'
    p = re.compile(restr)

    try:
    	bval = p.match(pwd_string)
    	return bval
    except Exception as e:
    	raise BadPasswordCharacter(e)

def clear_whitespace(s):
    p = re.compile(r'\s')
    return p.sub('', s)

def extract_from_equation(s):
    strip = clear_whitespace(s)
    restr = r'^(-?[0-9]+)/(-?[0-9]+)([+\-*/])(-?[0-9]+)/(-?[0-9]+)$'
    p = re.compile(restr)
    return p.findall(strip)

passwd = '8419DDSs'
print(strong_pwd(passwd))
s = 'This Is As Good As It Gets '
print(clear_whitespace(s))
e = '  -30/-534 * 20/40 '
print(extract_from_equation(e))