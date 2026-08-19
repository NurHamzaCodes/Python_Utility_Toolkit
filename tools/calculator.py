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

    num1 = int(input("Enter your number: "))
    if choice <5 :
        num2 = int(input("Enter your second number: "))


    match choice:
        case 1:
            add(num1,num2)
        case 2:
            sub(num1,num2)
        case 3:
            mul(num1,num2)
        case 4:
            div(num1,num2)
        case 5:
            sqr(num1)
        case 6:
            root(num1)