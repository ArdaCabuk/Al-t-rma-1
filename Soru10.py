k=0
for i in range(10000,100000):
    s=str(i)
    a=s[0]
    b=s[1]
    c=s[3]
    d=s[4]
    if int(a)==int(c) and int(b)==int(d):
        k=k+1
print(k)
    