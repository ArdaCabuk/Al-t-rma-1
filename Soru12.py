for i in range(1,2005):
    x=0
    for y in range(len(str(i))):
        x+=int(str(i)[y])
    if x==2005-i:
        print(i)
