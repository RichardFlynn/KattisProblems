from collections import Counter
turns=int(input())
bases=list(map(int,input().split()))
print((sum(bases)+Counter(bases)[-1])/(turns-Counter(bases)[-1]))