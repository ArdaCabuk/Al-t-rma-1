def factorial(n):
    if n < 2:
        return 1
    else:
        return n*factorial(n-1)
S=0
for i in range(1000):
    S=S+(1/factorial(i))
print("e=",S)
