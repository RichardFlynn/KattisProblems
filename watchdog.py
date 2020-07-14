for _ in range(int(input())):
    output="poodle"
    s,h=map(int,input().split())
    holes=[]
    for _ in range(h):
        holes.append(list(map(int,input().split())))
    print(holes)