points=[]
n=int(input())
for i in range(n):
    points.append(list(map(float,input().split())))
total=0
for i in range(n-1):
    total+=(points[i+1][0]-points[i][0])*(points[i+1][1]+points[i][1])/2
print("{:f}".format(total/1000))