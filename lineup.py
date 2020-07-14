incr=True
decr=True
n=int(input())
curr=input()
for _ in range(n-1):
    prev=curr
    curr=input()
    if prev<curr:
        decr=False
    else:
        incr=False
if incr:
    print("INCREASING")
elif decr:
    print("DECREASING")
else:
    print("NEITHER")