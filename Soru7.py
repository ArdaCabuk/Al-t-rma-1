L=[]
for i in range(100,1000):
    s=str(i)
    a=s[0]
    b=s[1]
    c=s[2]
    if int(a)+int(b)==int(c):
        L.append(i)
print(len(L))
print(L)        