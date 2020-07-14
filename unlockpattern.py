def measure(x,y):
    return ((x[0]-y[0])**2+(x[1]-y[1])**2)**0.5

c00,c01,c02=map(int,input().split())
c10,c11,c12=map(int,input().split())
c20,c21,c22=map(int,input().split())

nums={c00:(0,0),c01:(0,1),c02:(0,2),c10:(1,0),c11:(1,1),c12:(1,2),c20:(2,0),c21:(2,1),c22:(2,2)}

dis=0

for i in range(1,9):
    dis+=measure(nums[i],nums[i+1])
print("{:.10f}".format(dis))