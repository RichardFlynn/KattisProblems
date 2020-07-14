from math import ceil
students,target_grade=map(int,input().split())
grades=map(int,input().split())
if target_grade==100 and sum(grades)/students!=100:
    print("impossible")
else:
    print(ceil((students*target_grade-sum(grades))/(100-target_grade)))