gold,silver,copper=map(int,input().split())
total=3*gold+2*silver+copper
if total>7:
    print("Province or Gold")
elif total>5:
    print("Duchy or Gold")
elif total>4:
    print("Duchy or Silver")
elif total>2:
    print("Estate or Silver")
elif total>1:
    print("Estate or Copper")
else:
    print("Copper")