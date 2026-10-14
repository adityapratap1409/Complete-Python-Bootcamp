count=0
def power(a,n):
    result=1
    count=0
    for i in range(n):
        result=result*a
        count+=1
    return result
def power_recursively(a,n):
    count=0
    if n==0:
     return 1
    count+=1
    return a*power_recursively(a,n-1)
a=int(input("Enter the base "))
b=(int(input("Enter the exponent ")))

if b<0:
    print("Enter a non negative exponent")
else:
    print("Power ",power(a,b)," and count is ",count)
    print("Built in power ",a**b)
    print("Recursively ",power_recursively(a,b)," and count is ",count)