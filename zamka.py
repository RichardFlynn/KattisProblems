def dSum(n):
    total=0
    for d in str(n):
        total+=int(d)
    return total

lower_bound=int(input())
upper_bound=int(input())
digits_sum=int(input())

while dSum(lower_bound)!=digits_sum:
    lower_bound+=1
print(lower_bound)
while dSum(upper_bound)!=digits_sum:
    upper_bound-=1
print(upper_bound)