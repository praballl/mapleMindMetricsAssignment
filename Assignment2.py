# Star Pattern
num=5
for i in range(num,0,-1):
    for j in range(0,num-i):
        print(end=" ")
    if(i%2!=0):
        for j in range(0,i):
            if(j%2!=0):
                print("#",end=" ")
            else:
                print("*",end=" ")
    else:
        k=int(i/2)
        for j in range(0,k):
            if(j%2!=0):
                print("% $",end=" ")
            else:
                print("$ %",end=" ")
        
    print()