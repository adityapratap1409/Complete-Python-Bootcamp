import math

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
