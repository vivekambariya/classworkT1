# wrap to reverse the number and print the sum of the first and last digits of the number 
num = int(input("Enter a number: "))
temp = num  
rev = 0
while num > 0:
    last_digit = num % 10  
    print(last_digit, "is the last digit")
    rev = rev * 10 + last_digit 
    num = num // 10            
print("The reversed number is:", rev)

last_digit = temp % 10
first_digit = temp
while first_digit >= 10:
    first_digit = first_digit // 10
print("The sum of the first and last digits is:", first_digit + last_digit)
