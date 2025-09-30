#Q-1. Python program to check if the given number is Happy Number 
#A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly. 
#If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy 
#number. 
#Let's understand by an example: 
#Number = 32 
#32+ 22 = 13 
#12 + 32 = 10 
#12 + 02 = 1 
#So, 32 is a happy number.
num= int(input("Enter a number: "))

while num != 1 and num != 4:
    sum = 0 
    while num!=0:
            digit = num % 10
            sum += digit * digit
            num //= 10
    num = sum
   
if num == 1:
        print(num, "is a happy number")
else:
        print(num, "is not a happy number")
    
