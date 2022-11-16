for i in range(10,100):
    for x in range(10,100):
        if int(str(i)+str(x)) == 11*(x+i):
            print(i,x)
