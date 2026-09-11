import math
num=int(input("Enter number "))
c=0
if(num<0):
        print('Entered number is negative')
else:
        r=math.sqrt(num)
        rint=int(r)
        while(c!=0):
          if(rint==r):
             print('Entered number is a perfect square')
             continue
          else:
           print('Entered number is not a perfect square')
           c=1
print("Square root is ",r)