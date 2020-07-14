word=input()
per="PER"*int(len(word)/3)
count=0
for i in range(len(word)):
    if word[i]!=per[i]:
        count+=1
print(count)