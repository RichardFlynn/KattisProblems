from math import pi
for _ in range(int(input())):
    amp=input()
    nums=[]
    for c in amp:
        if c==" ":
            c=chr(91)
        elif c=="'":
            c=chr(92)
        nums.append(ord(c)-64)
    print(len(nums)+sum([min(abs(nums[i]-nums[i+1]),-abs(nums[i]-nums[i+1])%28)for i in range(len(nums)-1)])*pi/7)