def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
num=int(input("Enter the number "))
print("The factorial of ",num," is",factorial(num))
#that was a recursive function the normal way would be like this
def factoria(x):
    factori=1
    i=x
    while(i>0):
        factori=factori*i
        i-=1
    return factori
print("The factorial of ",num," is",factoria(num))
'''def add(*b):
    result=0
    for i in b:
        result=result+i
    return result
print(add(10,20,30))
print(add(1,2,3,4,5,6,7,8,9,10))
print(add(10,20,30,40,50))
def course(**a):
    for i in a.items():
        print(i)
course(year=2026,college_name="VIT Bhopal",semester="First semester")
def sum(n):
    if n>1:
        return n+sum(n-1)
    return 1
num=int(input("Enter the number: "))
print("The sum is: ",sum(num))'''