intervals=int(input())
while intervals!=-1:
    prev_time=0
    distance=0
    for _ in range(intervals):
        speed,time=map(int,input().split())
        distance+=speed*(time-prev_time)
        prev_time=time
    print(distance,"miles")
    intervals=int(input())