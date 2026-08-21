import random
import string

def pasw():
    
    while True:
        digit_number = int(input("\nHow many digit you want to set your password: "))
        if digit_number >= 4 and digit_number<=20:
            break

        elif digit_number > 20:
            print("Waring: You have must lower or equal then 20 character in your password. ")

        else:
            print("Waring: You have must greater or equal then 4 character in your password.")

    print()
    op1 = input("Are you want any upper case in your password  (y/n): ")
    op2 = input("Are you want any number digit in your password (y/n): ")
    op3 = input("Are you want any simbol in your password (y/n): ")

    p = [
        list(string.ascii_lowercase),
        list(string.ascii_uppercase),
        list(string.digits),
        list("!@#$&_")
    ]
    password = []

    for i in range(0,4,1):
        random.shuffle(p[i])

    count = 0

    if op1 == "n" and op2 == "n" and op3 == "n":
        for i in range(1,digit_number+1):
            password.append(p[0][i-1])

    elif op1 == "n" and op2 == "n":
        for _ in range(1,digit_number+1,2):
            password.extend([p[0][count],p[3][count],])
            count+=1

    elif op1 == "n" and op3 == "n":
        for _ in range(1,digit_number+1,2):
            password.extend([p[0][count],p[2][count]])
            count+=1

    elif op2 == "n" and op3 == "n":
        for _ in range(1,digit_number+1,2):
            password.extend([p[0][count],p[1][count]])
            count+=1

    elif op1 == "n":
        for _ in range(1,digit_number+1,3):
            password.extend([p[0][count],p[2][count],p[3][count]])
            count+=1

    elif op2 == "n":
        for _ in range(1,digit_number+1,3):
            password.extend([p[0][count],p[1][count],p[3][count]])
            count+=1

    elif op3 == "n":
        for _ in range(1,digit_number+1,3):
            password.extend([p[0][count],p[1][count],p[2][count]])
            count+=1

    else:
        for _ in range(1,digit_number+1,4):
            password.extend([p[0][count],p[1][count],p[2][count],p[3][count]])
            count += 1

    random.shuffle(password)

    print("\nYour password: ","".join(password))
