N,W,H=map(int,input().split())
big=(W*W+H*H)**0.5
for _ in range(N):
    if int(input())<=big:
        print("DA")
    else:
        print("NE")