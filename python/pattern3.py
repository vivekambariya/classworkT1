for i in range(5):
    count=65
    for j in range(4-i):
        print("", end=" ")
    for k in range(i+1):
        print(chr(count), end=" ")
        count+=1
    print( )

#    A 
#   A B 
#  A B C
# A B C D
#A B C D E






