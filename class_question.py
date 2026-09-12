'''n=int(input("Enter a number to check even odd "))
if(n%2==0):
    print(n," Is even")
else:
    print(n,' Is odd')
n=int(input("Enter a number to check negative and positive "))
if(n>0):
    print(n,' is a positive number')
elif(n<0):
    print(n,' is a negative number')
else:
    print(n, ' is zero')
age=int(input("Enter your age "))
if(age<18):
    print(age, ' is not a valid age to vote')
else:
    print(age, 'is a valid age to vote')
first = int(input("Enter first number: "))
second = int(input("Enter your second number: "))
third = int(input("Enter your third number: "))
fourth = int(input("Enter your fourth number: "))
if (first > second and first > third and first > fourth):
     greatest = "First is greatest"
elif (second > third and second > fourth):
     greatest = "Second is greatest"
elif (third > fourth):
     greatest = "Third is greatest"
else:
     greatest = "Fourth is greatest"
print (greatest)
year=int(input("Enter a year to find if its leap year or not "))
if(year%400==0 or (year%4==0 and year%100==0)):
    print(year," is a leap year")
else:
    print(year," is not a leap year")
purchase_amount=int(input("Enter your total purchase amount "))
if(purchase_amount>2000):
    purchase_amount-=500
print(purchase_amount," is the amount you to pay")'''
for i in range (1,11):
    print(i,end=" ")
print(" ")
for i in range (2,21):
    if(i%2==0):
        print(i,end=" ")
print(" ")
for i in range (1,22):
    if(i%2!=0):
        print(i,end=" ")
print(" ")
for i in range(20,0,-2):
    print(i,end=" ")
print(" ")
n=int(input("Enter a number to check if its prime or not "))
boole=True
for i in range(2,n):
    if(n%i==0):
        boole=False
        break
if(boole):
    print("Entered number is prime")
else:
    print("Entered number is not prime")