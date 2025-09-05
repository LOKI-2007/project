number1=int(input("enter first number"))
number2=int(input("enter second number"))
number3=int(input("enter third number"))
if number1<number2:
    print("number1 is minimum number")
elif number2<number3:
    print("number2 is minimum number")
elif number3<number1:
    print("number3 is minimum number")
else:
    print("maximum number")