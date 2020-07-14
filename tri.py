n1,n2,n3=input().split()
if int(n1)+int(n2)==int(n3):
    print(n1+"+"+n2+"="+n3)
elif int(n1)==int(n2)+int(n3):
    print(n1+"="+n2+"+"+n3)
elif int(n1)*int(n2)==int(n3):
    print(n1+"*"+n2+"="+n3)
elif int(n1)==int(n2)*int(n3):
    print(n1+"="+n2+"*"+n3)
elif int(n1)/int(n2)==int(n3):
    print(n1+"/"+n2+"="+n3)
elif int(n1)==int(n2)/int(n3):
    print(n1+"="+n2+"/"+n3)
elif int(n1)-int(n2)==int(n3):
    print(n1+"-"+n2+"="+n3)
elif int(n1)==int(n2)-int(n3):
    print(n1+"="+n2+"-"+n3)