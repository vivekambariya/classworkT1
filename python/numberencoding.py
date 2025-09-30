#write a program to encode a number based on follwing rule
#1=3, 2=4, 3=5 ,4=6 ,5=7, 6=8, 7=9, 8=1, 9=2, 0=0
num = int(input("Enter a number to encode: "))

encoded = 0
place = 1

while num > 0:
    digit = num % 10

    if digit == 1:
        new_digit = 3
    elif digit == 2:
        new_digit = 4
    elif digit == 3:
        new_digit = 5
    elif digit == 4:
        new_digit = 6
    elif digit == 5:
        new_digit = 7
    elif digit == 6:
        new_digit = 8
    elif digit == 7:
        new_digit = 9
    elif digit == 8:
        new_digit = 1
    elif digit == 9:
        new_digit = 2
    elif digit == 0:
        new_digit = 0

    encoded = encoded + new_digit * place
    place *= 10
    num //= 10

print("Encoded number:", encoded)

