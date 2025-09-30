#you are adding money in you pigibank starting from monday with rupees 1 and increase 1 rupees in each day of the week 
#next monday you start with rupees 2 and increase 1 rupees in each day 
#follow same logic for all weeks wap to print amonunt of money in your pigibank after number of days user enters
days = int(input("enter number of days: "))

money = 1
sundays = 7
total = 0
for i in range(days//7):
        for j in range(money,sundays+1):
            total += j
            money += 1
    
        sundays += 7
for k in range(days%7):
        total += money
        money += 1
  

  # this code is half