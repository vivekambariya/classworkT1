#write a program which stats date month and year of a day and print the day of the next day
#also check if the entered day by the user is valid or not.
Date = input("Enter the date in the format dd/mm/yyyy: ")
if len(Date) == 10:
    day, month, year = Date.split('/')
    if day.isdigit() and month.isdigit() and year.isdigit():
        day = int(day)
        month = int(month)
        year = int(year)
        if day >= 1 and day <= 31 and month >= 1 and month <= 12 and year >= 1 and year <= 2025:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                if day == 31:
                    day = 1
                    if month == 12:
                        month = 1
                        year += 1
                    else:
                        month += 1
                else:
                    day += 1
            elif month == 4 or month == 6 or month == 9 or month == 11:
                if day == 30:
                    day = 1
                    month += 1
                elif day < 30:
                    day += 1
                else:
                    print("Invalid date")
                    exit()
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    if day == 29:
                        day = 1
                        month += 1
                    elif day < 29:
                        day += 1
                    else:
                        print("Invalid date")
                        exit()
                else:
                    if day == 28:
                        day = 1
                        month += 1
                    elif day < 28:
                        day += 1
                    else:
                        print("Invalid date")
                        exit()
            else:
                print("Invalid date")
                exit()
            print("Next date is: ", day, "/", month, "/", year)
        else:
            print("Invalid date")
    else:
        print("Invalid input: day, month and year must be numbers.")
else:
    print("Invalid input format: please enter date as dd/mm/yyyy.")