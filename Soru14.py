c = 121212
for i in range (1,121213):
    for a in range(1,121213):
        if i*a == 121212:
            if c > abs(i-a):
                c = abs(i-a)