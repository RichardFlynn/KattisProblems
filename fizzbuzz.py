x,y,n=map(int,input().split())
for i in range(1,n+1):
    fb=""
    if i%x==0:
        fb+="Fizz"
    if i%y==0:
        fb+="Buzz"
    if fb=="":
        fb=i
    print(fb)