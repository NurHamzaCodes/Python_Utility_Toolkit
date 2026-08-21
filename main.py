import work

def opening():
    print(34*"=")
    print("||    Python Utility Toolkit    ||")
    print(34*"=")

    print("\nChoose what do you want: \n\n1. Calculator\n2. Unit Converte\n3. Password Generator\n4. Date tools\n")
    choice = int(input("What is your choice: "))

    return choice

if __name__ == "__main__":
    choice = opening()
    work.works(choice)

    print()
