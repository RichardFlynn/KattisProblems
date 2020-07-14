cipher,key=(input() for _ in range(2))
for i in range(len(cipher)):
    key+=chr((ord(cipher[i])-ord(key[i]))%26+65)
print(key[len(key)-len(cipher):])