count=0
for _ in range(int(input())):
    button=input().lower()
    if "pink" in button or "rose" in button:
        count+=1
if count==0:
    print("I must watch Star Wars with my daughter")
else:
    print(count)