limit=int(input())
months=int(input())
total=limit*months+limit
for _ in range(months):
    total-=int(input())
print(total)