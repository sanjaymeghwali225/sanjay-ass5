asciichr = 65

for i in range(0,5):
     for j in range(0,i+1):
         char = chr(asciichr)
         print(char,end="")
         asciichr += 1
     print()