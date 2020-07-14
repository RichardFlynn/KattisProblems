message=input()
decryp_key=input()
secret=""
for i in range(len(message)):
    secret+=chr((ord(message[i])-((-1)**i)*ord(decryp_key[i])-130)%26+65)
print(secret)