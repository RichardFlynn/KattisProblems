def button(x):
    if x==0:
        return 0
    if x==1:
        return 1
    if nums[x]!=0:
        return nums[x]
    nums[x]=button(x-1)+button(x-2)
    return nums[x]

n=int(input())
nums=[0 for i in range(n+1)]
print(button(n-1),button(n))