S=0
for i in range(1,100000):
    S=S+1/i**2
print("pi=",(6*S)**(1/2))
