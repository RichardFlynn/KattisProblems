for _ in range(int(input())):
    b,p=map(float,input().split())
    print('{:.4f}'.format(b*60/p-60/p),'{:.4f}'.format(b*60/p),'{:.4f}'.format(b*60/p+60/p))