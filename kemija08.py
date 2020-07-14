word=input()
for v in ("a","e","i","o","u"):
    word=word.replace("{}p{}".format(v,v),"{}".format(v))
print(word)