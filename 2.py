x=("Range :-\n")
print(x)

a=int(input("From :-\n"))
b=int(input("To where :-\n"))
c=int(input("Number from which divisible :-\n"))

for r in range(a+1,b+1):
    if (r%c==0):
       print(r)
