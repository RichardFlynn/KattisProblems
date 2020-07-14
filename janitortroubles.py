from math import cos, pi
a,b,c,d=map(int,input().split())
#d1**2=a**2+b**2-2abcosA
#d1**2=c**2+d**2-2cdcosC
#a**2+b**2-2abcosA=c**2+d**2-2cdcosC
#a**2+b**2-(c**2+d**2)=2(abcosA-cdcosC)
#d2**2=a**2+d**2-2adcosD
#d2**2=c**2+b**2-2cbcosB
s=(a+b+c+d)/2
#Area=((s-a)(s-b)(s-c)(s-d)-0.5abcd(1+cos(A+C)))**0.5
print(((s-a)*(s-b)*(s-c)*(s-d)-0.5*a*b*c*d*(1+cos(pi)))**0.5)