input()
nums=map(int,input().split())
print(-sum([x for x in nums if x<0]))