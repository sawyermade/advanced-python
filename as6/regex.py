import re
# if you need any other imports, put them below


class BadPasswordCharacter(Exception):
    pass

class InvalidFractionExpression(Exception):
    pass

def strong_pwd(pwd_string):
    restr = r'^(?=[a-zA-Z0-9]*[a-z][a-zA-Z0-9]*)(?=[a-zA-Z0-9]*[A-Z][a-zA-Z0-9]*)(?=[a-zA-Z0-9]*[0-9][a-zA-Z0-9]*)[a-zA-Z0-9]{8,}$'
    p = re.compile(restr)

    if p.match(pwd_string):
        return True  
    else:
        raise BadPasswordCharacter('Password Not Strong Enough.')

def clear_whitespace(s):
    p = re.compile(r'\s')
    return p.sub('', s)

def extract_from_equation(s):
    strip = clear_whitespace(s)
    restr = r'^(-?[0-9]+)/([0-9]+)([+\-*/])(-?[0-9]+)/([0-9]+)$'
    p = re.compile(restr)

    if p.match(strip):
        return p.findall(strip)[0]
    else:
        raise InvalidFractionExpression('Fraction Expression is Invalid.')

if __name__ == '__main__':
    passwd = '1984DDs!'
    try:
        strong_pwd(passwd)
        print('Password is Strong Enough')
    except BadPasswordCharacter as e:
        print(e)
    passwd = '1984DDss'
    try:
        strong_pwd(passwd)
        print('Password is Strong')
    except BadPasswordCharacter as e:
        print(e)

    s = 'This Is As Good As It Gets '
    print(clear_whitespace(s))

    e = '  -30/534 * 20/40 '
    print(extract_from_equation(e))

    e = ' -30/500 + 1'
    try:
        print(extract_from_equation(e))
    except InvalidFractionExpression as e:
        print(e)