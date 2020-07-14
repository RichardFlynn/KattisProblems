from math import pi
def reverseVol(baseDia,vol):
    return ((vol-(pi/12)*baseDia**3)/(pi/6))**(1/3)
def cylVol(baseDia):
    return pi*baseDia**3/4

dia,vol=map(int,input().split())
while dia+vol!=0:
    print("{:.9f}".format(reverseVol(dia,cylVol(dia)-vol)))
    dia,vol=map(int,input().split())