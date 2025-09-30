num = float(input("enter the number : ")) 
if (num>=0 and num<=1):
    num = num*100
    if num>=25:
        a=num//25
        print(a,"quaters",end=" ")
        num=num%25
    if  num>=10:
        a=num//10
        print(a,"dime",end=' ')
        num=num%10
    if num>=5:
        a=num//5
        print(a,"nickel",end=' ')
        num=num%5
    else :
        print(num,"penny")
else :
    print("the number is not in the range")       
