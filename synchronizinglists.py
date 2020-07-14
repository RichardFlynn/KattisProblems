def quicksort(l,r):
    if r-l<=0:
        return
    part=partition(l,r,mylist1[r])
    quicksort(l,part-1)
    quicksort(part+1,r)
def partition(l,r,p):
    rptr=r-1
    while True:
        while mylist1[l]<p:
            l+=1
        while mylist1[rptr]>=p and rptr>0:
            rptr-=1
        if l>=rptr:
            break
        swap(l,rptr)
    swap(l,r)
    return l
def swap(s1,s2):
    temp1=mylist1[s1]
    temp2=mylist2[s1]
    mylist1[s1]=mylist1[s2]
    mylist2[s1]=mylist2[s2]
    mylist1[s2]=temp1
    mylist2[s2]=temp2

n=int(input())
while n!=0:
    mylist1=[int(input())for _ in range(n)]
    mylist2=[x for x in range(n)]
    quicksort(0,n-1)
    order=mylist2
    mylist2=[0 for _ in range(n)]
    mylist1=[int(input())for _ in range(n)]
    quicksort(0,n-1)
    correct=[0 for _ in range(n)]
    for i in order:
        correct[i]=mylist1.pop(0)
    for num in correct:
        print(num)
    n=int(input())