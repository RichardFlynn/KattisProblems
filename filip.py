def flip(s):
    t=""
    for c in s:
        t=c+t
    return int(t)
num1,num2=map(flip,input().split())
print(max(num1,num2))