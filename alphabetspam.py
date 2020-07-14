spam=input()
whitespace=0
lowercase=0
uppercase=0
symbol=0
for c in spam:
    if ord(c)==95:
        whitespace+=1
    elif ord(c)<65:
        symbol+=1
    elif ord(c)<91:
        uppercase+=1
    elif ord(c)<97:
        symbol+=1
    elif ord(c)<123:
        lowercase+=1
    else:
        symbol+=1
print("{:.16f}".format(whitespace/len(spam)))
print("{:.16f}".format(lowercase/len(spam)))
print("{:.16f}".format(uppercase/len(spam)))
print("{:.16f}".format(symbol/len(spam)))