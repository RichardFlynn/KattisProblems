scales=['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
tones=[0,2,4,5,7,9,11]
n=input()
notes=set(input().split())
out=[]
for scale in range(12):
    s=[scales[(scale+i)%12]for i in tones]
    b=True
    for n in notes:
        if n not in s:
            b=False
            break
    if b:
        out+=[scales[scale]]
if out==[]:
    print("none")
else:
    print(*out)