t=0
for _ in range(int(input())):
    n=input()
    t+=int(n[0:-1])**int(n[-1:])
print(t)