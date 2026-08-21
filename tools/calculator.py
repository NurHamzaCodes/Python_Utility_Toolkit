import math

add = lambda num1,num2 : num1+num2
sub = lambda num1,num2 : num1-num2
mul = lambda num1,num2 : num1*num2
div = lambda num1,num2 : num1/num2
sqr = lambda num : num*num
root = lambda num : math.sqrt(num)

def cal():
    print("What the kind of your calculation: \n\n1.Addition        2.Subtraction\n3.Multiplication  4.Divition\n5.Squre           6.Root\n")
    choice = int(input("What do you calculation: "))

    num1 = int(input("\nEnter your number: "))
    if choice <5 :
        num2 = int(input("Enter your second number: "))


    match choice:
        case 1:
            ans = add(num1,num2)
            print("\nThe result: ",ans)
        case 2:
            ans = sub(num1,num2)
            print("\nThe result: ",ans)
        case 3:
            ans = mul(num1,num2)
            print("\nThe result: ",ans)
        case 4:
            ans = div(num1,num2)
            print("\nThe result: ",ans)
        case 5:
            ans = sqr(num1)
            print("\nThe result: ",ans)
        case 6:
            ans = root(num1)
            print("\nThe result: ",ans)