#Write a prgram to take the user input for hour between and hour between 1 abnd 12
#and takes the user input and of am and pm and also take the user input of how many hour into the future we want to print  
#print out the time in the future by calculating hours enterd by the user 
def future_time():
    hour = int(input("Enter the hour between 1 and 12: "))
    am_pm = input("Enter AM or PM: ")
    future_hour = int(input("Enter the number of hours into the future: "))

    for i in range (1,future_hour+1):
    
        hour += 1
        if hour > 12:
                hour = hour>1
        if hour==12 :
            if am_pm == "AM":
                    am_pm = "PM"
            elif am_pm=="PM":
                    am_pm = "AM"
    print(f"The time in the future is {hour} {am_pm}")

future_time()            