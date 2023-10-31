import re
patt = re.compile('^(?:[( )-]*\d){10}[()-]*$')
sovp = re.findall(patt, '(050)280-31-42')
print(sovp)

if sovp != []:
    while not sovp[0].isdigit():
        check_dig = sovp[0]
        for char in check_dig:
            if not char.isdigit():
                sovp[0] = sovp[0].replace(char, '')
else:
    raise ValueError

dict_rec = {'qqq': 'ewrewr'}
print(dict_rec)

# a = sovp[0]
# b = a.replace(')', '')
# print(b)
