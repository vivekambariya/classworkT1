a=int(input("enter the number 1 "))
b=int(input("enter the number 2 "))
c=int(input("enter the number 3 "))
if a>b and a>c:
    if b>c:
        print("descending",a,b,c)
        print("ascending",c,b,a)
    else :
        print("descending",a,c,b)
        print("ascending",b,c,a)
elif b>a and b>c :
    if a>c :
        print("descending",b,a,c)
        print("ascending",c,a,b)
    else :
        print("descending",b,c,a)
        print("ascending",a,c,b)
else :
    if a>b:
        print("descending",c,a,b)
        print("ascending",b,a,c)
    else :
        print("descending",c,b,a)
        print("ascending",a,b,c)    