#Q-2 Python Program to Find All Pythagorean Triplets in the Range pythagorean triplets are the three 
#numbers which follows pythagoros therom, a^2+b^2=c^2 -->then a,b,c is triplets. 
#Enter upper limit:10 
#3 4 5 
#8 6 10 
#Enter upper limit:20 
#3 4 5 
#8 6 10 
#5 12 13 
#15 8 17 
#12 16 20
limit = int(input("Enter upper limit: "))

for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            if (a*a + b*b) == c*c:
                print(a, b, c)
