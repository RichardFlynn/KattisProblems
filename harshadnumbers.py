def isHarshad(num):
    if num%sum(map(int,str(num)))==0:
        return True
    return False

n=int(input())
while not isHarshad(n):
    n+=1
print(n)