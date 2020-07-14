h,m=map(int,input().split())
if m<45:
    h-=1
    m+=60
print(h%24,m-45)