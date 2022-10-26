L=[]
for i in range(100,1000,2):
    s=str(i)
    a=s[0]
    b=s[1]
    c=s[2]
    if int(a)==int(b) or int(b)==int(c) or int(c)==int(a):
        L.append(i)
print(len(L))
