import math
import random

number = float(input("Enter a number "))
print(number**0.5)
print(math.sqrt(number))
print(math.pow(number, 0.5))


def newtonsqrt(nu):
    root = nu / 2
    for i in range(10):
        root = (root + nu / root) / 2
    return root


print(newtonsqrt(number))


def print_factors(nu):
    print(f"\nThe factors of {nu} are: ", end="")
    for i in range(1, nu + 1):
        if nu % i == 0:
            print(i, end=" ")


num = int(input("Enter number to find its factors: "))
print_factors(num)


def print_smallest_factor(nu):
    print(f"\nThe smallest factor of {nu} is: ", end="")
    for i in range(1, nu + 1):
        if nu % i == 0 and i != 1:
            print(i)
            break


print_smallest_factor(num)


def compute_hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if (x % i == 0) and (y % i == 0):
            hcf = i
    return hcf


def gcd(a, b):
    dividend = a
    divisor = b
    if b > a:
        dividend = b
        divisor = a
    if a == b:
        return a
    while divisor > 0:
        remainder = dividend % divisor
        dividend = divisor
        divisor = remainder
    return dividend


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("\nThe H.C.F is ", compute_hcf(num1, num2))
print(f"The gcd of {num1} and {num2} is: {gcd(num1,num2)}")
print(math.gcd(num1, num2))


def compute_lcm(n1, n2):
    if n1 > n2:
        higher = n1
    else:
        higher = n2
    value = higher
    while True:
        if higher % n1 == 0 and higher % n2 == 0:
            print(f"LCM of {n1} and {n2} is {higher}")
            break
        else:
            higher += value


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
compute_lcm(num1, num2)
t1, t2 = num1, num2
while num2 > 0:
    r = num1 % num2
    num1 = num2
    num2 = r

GCD = num1
LCM = (t1 * t2) // GCD
print("LCM is ", LCM)
print("GCD is ", GCD)
lower = int(input("Set lower limit: "))
upper = int(input("Set upper limit: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
    else:
        print(num)

n = int(input("Enter n : "))
count = 1
num = 2
while count <= n:
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            print(num)
            count += 1
        num += 1

x = eval(input("Enter number: "))
while x != 1:
    for i in range(2, x + 1):
        if x % i == 0:
            print(i)
            x //= i
            print(x, end=" ")
            break
print(random.randrange(10))
print(random.randrange(10, 20))
print(random.randrange(100, 200, 2))
print(random.randint(1, 10))
print(random.random())
print(random.uniform(0.5, 1.5))
print(random.choice("VITBHOPAL"))

deck = list(range(1, 52))
print(deck)
random.shuffle(deck)
print(deck)
hand = random.sample(deck, k=5)
print(hand)


def power(a, n):
    result = 1
    for i in range(n):
        result = result * a
    return result


def power_recursively(a, n):
    if n == 0:
        return 1
    return a * power_recursively(a, n - 1)


a = int(input("Enter the base "))
b = int(input("Enter the exponent "))

if b < 0:
    print("Enter a non negative exponent")
else:
    print("Power ", power(a, b))
    print("Built in power ", a**b)
    print("Recursively ", power_recursively(a, b))