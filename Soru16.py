def asal_mi(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0 :
            return False
    return True
a = int(input("Sayı: "))
if asal_mi(a):
    print(a,"sayısı asaldır.")
else:
    print(a,"sayısı asal değildir.")