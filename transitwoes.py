start,end,buses=map(int,input().split())
bus_distances=list(map(int,input().split()))
bus_journey_times=list(map(int,input().split()))
bus_arrival_times=list(map(int,input().split()))

for i in range(buses):
    start+=bus_distances[i]
    start+=(bus_arrival_times[i]-start%bus_arrival_times[i])%bus_arrival_times[i]
    start+=bus_journey_times[i]
    
if start+bus_distances[buses]<=end:
    print("yes")
else:
    print("no")