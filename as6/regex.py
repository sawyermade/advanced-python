import re
# if you need any other imports, put them below


class BadPasswordCharacter(Exception):
    pass

class InvalidFractionExpression(Exception):
    pass

def strong_pwd(pwd_string):
    restr = r'(?=\w*[a-z]\w*)(?=\w*[A-Z]\w*)(?=\w*\d\w*)\w{8,}'
    p = re.compile(restr)

    try:
    	bval = p.match(pwd_string)
    	return bval
    except Exception as e:
    	raise BadPasswordCharacter(e)

def clear_whitespace(s):
    p = re.compile(r'[ ]*')
    return p.sub('', s)


def extract_from_equation(s):
    pass # replace this with the real code

passwd = '841D'
s = 'This Is As Good As It Gets '
print(clear_whitespace(s))
