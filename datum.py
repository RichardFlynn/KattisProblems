days=["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]
months=[31,28,31,30,31,30,31,31,30,31,30,31]
d,m=map(int,input().split())
print(days[(sum(months[:m-1])+d)%7])