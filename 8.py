list1 = []
e=0
o=0
p=0
n=0

for i in range(10):
     num = int(input("Enter an integer:"))
     list1.append(num)

for j in list1:
     if j>0:
         p+=1
     else:
         n+=1
     if j%2==0:
         e+=1
     else:
         o+=1

def countx(lst, x):
     count = 0
     for ele in lst:
         if (ele == x):
             count = count + 1
     return count

print(p,"positive numbers\n")
print(n,"negative numbers\n")
print(e,"even numbers\n")
print(o,"odd numbers\n")

x=int(input("Enter the number you want to know count of:"))
print(countx(list1,x))