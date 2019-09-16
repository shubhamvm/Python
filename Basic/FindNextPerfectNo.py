a = int(input("Enter a: "))
b = int(input("Enter b: "))

x = a+b
y = x*x
flag = True

if (a>0,b>0):
    for i in range(x+1,y):
        for j in range(2,i):
            if ((i%j)==0):
                flag=False
                break
            else:
                flag=True
        if (flag==True):
            print(i-x)
            break
else:
    print("Number greater than zero")
