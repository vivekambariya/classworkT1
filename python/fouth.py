#write a program to enter a number 
#that prompt user and stops only when user enter done after this print the average of the number
# and minimum and maximum number from all the numbner enter by the user

print("Enter numbers one by one. Type 'done' to finish.")

total = 0
count = 0
maximum=None
minimum=None

while True:
    user_input = input("Enter a number (or 'done'): ")
    
    if user_input == "done":
        break
    else:
            num = int(user_input)
            
            total += num
            count += 1
            
            if  num==None or num < minimum:
                minimum = num
                
            if  num==None or num > maximum:
                maximum = num
        
if count > 0:
    average = total / count
    print("Average :", average)
    print("Minimum :", minimum)
    print("Maximum :", maximum)
else:
    print("numbers are not entered.")