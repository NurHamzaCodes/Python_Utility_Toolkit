def conv():
    print("What do you want to converter:\n\n1.Meter to Feet          2.Feet to Meter\n3.Kilogram to Pound      4.Pound to kilogram\n5.Celsius to Fahrenheit  6.Fahrenheit to Celsius\n")
    choice = int(input("What is your choice: "))

    intp = int(input(("\nInput the measurement: ")))

    match choice:
        case 1:
            print("The Feets: ",intp*3.28084)
        case 2:
            print("The Meteris: ",intp*0.3048)
        case 3:
            print("The Pound: ",intp*2.20462)
        case 4:
            print("The Kilogram: ",intp*0.453592)
        case 5:
            print("The Fahrenheits: ",(intp*9/5) + 32)
        case 6:
            print("The Celsius: ",(intp - 32)*5/9)