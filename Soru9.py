def toplambulma(n):    
    toplam = 0
    for x in str(n): 
      toplam += int(x)      
    return toplam
   
for i in range(1,1000):
    s=toplambulma(i)
    if int(s)<9:
        print(str(i),end =" ")