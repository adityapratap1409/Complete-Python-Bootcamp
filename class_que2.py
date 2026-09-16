import math
n=int(input("Enter a number to check negative and positive "))
if(n>0):
    print(n,' is a positive number')
elif(n<0):
    print(n,' is a negative number')
else:
    print(n, ' is zero')
#To find roots of quadratic equation
a=int(input("Enter the coffecient of x^2 "))
b=int(input("Enter the coffecient of x "))
c=int(input("Enter the constant term "))
D=(b**2)-4*(a*c)
if(D>=0):
 square_Root=math.sqrt(D)
 Final_answer1=((-b)+square_Root)/(2*a)
 Final_answer2=((-b)-square_Root)/(2*a)
 print(Final_answer1)
 print(Final_answer2)
else:
    print("Roots are imaginary")
light_colour=input("Enter light colour ")
if(light_colour=="red" or light_colour=="Red"):
    print("STOP")
elif(light_colour=="green" or light_colour=="Green"):
    print("GO")
elif(light_colour=="yellow" or light_colour=="Yellow"):
    print("LOOK")
else:
    print("Wrong input")
