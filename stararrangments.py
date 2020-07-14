def check(num1,num2):
    if stars%(num1+num2)==0 or (stars-num1)%(num1+num2)==0:
        print("{},{}".format(num1,num2))

stars=int(input())
print("{}:".format(stars))
for i in range(2,stars):
    check(i,i-1)
    check(i,i)