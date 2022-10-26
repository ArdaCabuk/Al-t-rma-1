L=[]
for i in range(1000,10000):
    s=str(i)
    a=s[0]
    b=s[3]
    if a>b:
        L.append(i)
print(len(L))        