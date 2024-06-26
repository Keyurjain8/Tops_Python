n1 = 0 
n2 = 1
i = 1
n3=n1 + n2
for i in range(1 ,8):
    n1=n2
    n2=n3
    n3 = n1 + n2
    i+=1
    
    print(f"{n3}",end=" ")
