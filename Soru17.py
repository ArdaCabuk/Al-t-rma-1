def palindromik_mi(x):
    if x == x[::-1]:
        print(x,"sayısı palindromiktir.")
    else:
        print(x,"sayısı palindromik değildir.")
a = input("Bir sayı giriniz:")
palindromik_mi(a)