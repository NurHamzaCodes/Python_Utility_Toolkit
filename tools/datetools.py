import datetime

def date():
    print("\nWhat kind of tools you want: \n\n1.Current Date & Time\n2.Date Different\n3.Day of Week\n4.Is Leap Year\n")
    choice = int(input("\nWhat do you want: "))

    match choice:
        case 1:
            print("Date: ", datetime.datetime.day().strftime("%d-%m-%Y"))
            print("Time: ", datetime.datetime.now().strftime("%H:%M:%S"))

        case 2:
            print("Enter first date:")
            year1 = int(input("Year: "))
            month1 = int(input("Month: "))
            day1 = int(input("Day: "))

            print("\nEnter second date:")
            year2 = int(input("Year: "))
            month2 = int(input("Month: "))
            day2 = int(input("Day: "))

            date1 = datetime.date(year1, month1, day1)
            date2 = datetime.date(year2, month2, day2)

            difference = date2 - date1

            print("Difference:", difference.days, "days")


        case 3:
            print("Enter date:")
            year = int(input("Year: "))
            month = int(input("Month: "))
            day = int(input("Day: "))

            date = datetime.date(year,month,day)
            print("This day is: ",date.strftime("%A"))

        case 4:
            year = int(input("Input the year: "))

            if (year%4 == 0 and year%100 != 0) or year%400 == 0:
                print("It is a leap year.")

            else:
                print("It is not a leap year.")