for i in range(10000,100000):
    a = 0
    for b in range(2,int(i**0.5)+1):
        if i % b == 0:
            a += 1
    if a == 0:
        print(i)