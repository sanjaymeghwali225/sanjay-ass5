import math
a=int(input("Enter the first side of tringle:-\n"))
b=int(input("Enter the secound side of tringle:-\n"))
c=int(input("Enetr the third side of tringle:-\n"))

if a+b<c or a+c<b or b+c<a:
    print("Tringle is not possible")
    
else:
    print("Tringle is possible")
    d=(a+b+c)/2
    area=math.sqrt(d*(d-a)*(d-b)*(d-c))
    print(area)

