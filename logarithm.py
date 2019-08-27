import math
def logFunc(x=10):
     if x <=  0:
         print ("X is not a integer")
     else:
         res= math.log(x)
         return res


x = int(input("enter a number"))
log = logFunc(x)
print (log)