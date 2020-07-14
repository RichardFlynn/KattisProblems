import numpy

def diag(a,b,c):
    if b<0 or b>len(a)-1:
        return 0
    return a[c][b]
    
for _ in range(int(input())):
    output=[]
    d0=int(input())+1
    a_list0=list(map(lambda x:[int(x)],input().split()))
    d1=int(input())+1
    a_list1=list(map(int,input().split()))
    #print(a_list0,a_list1)
    while len(a_list0)<max(d0,d1):
        a_list0.append(0)
    while len(a_list1)<max(d0,d1):
        a_list1.append(0)
    a_list0=numpy.array(a_list0)
    a_list1=numpy.array([a_list1])
    #print(a_list0,a_list1)
    m=numpy.dot(a_list0,a_list1)
    #print(m)
    for c in range(2*len(m)+1):
        output.append(sum(diag(m,c-r,r)for r in range(len(m))))
    while output[len(output)-1]==0:
        output=output[:len(output)-1]
    print(len(output)-1)
    print(*output)