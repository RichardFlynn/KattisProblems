from collections import Counter
c=Counter(input())
print(c['T']*c['T']+c['C']*c['C']+c['G']*c['G']+7*min(c['T'],c['C'],c['G']))