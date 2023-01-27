nl=[]
for x in range(1,501):
     if (x%7==0) and (x%11==0):
         nl.append(str(x))
print (','.join(nl))