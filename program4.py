number=int(input("enter number"))
flag=True
for i in range(2,number):
    if number%i==0:
        flag=False


if(flag==True):
    print("prime number")
else:
    print("not prime number")
