n = int(input("Enter a number: "))
num = n
print(f"Prime factors of {n} are:", end=" ")
d = 2
while d * d <= num:
    while num % d == 0:
        print(d, end=" ")
        num //= d
    d += 1
if num > 1:
    print(num, end=" ")
print()
N = int(input("\nEnter N: "))

print(f"Prime numbers less than {N}:", end=" ")
for num in range(2, N):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
bill = float(input("\nEnter total bill amount: Rs. "))
if bill > 25000:
    discount_pct = 50
elif bill >= 20001:
    discount_pct = 40
elif bill >= 15001:
    discount_pct = 30
elif bill >= 10001:
    discount_pct = 20
elif bill >= 5001:
    discount_pct = 10
else:
    discount_pct = 0
discount_amount = bill * discount_pct / 100
final_amount = bill - discount_amount
print(f"Original Bill: Rs.{bill}")
print(f"Discount Applied: {discount_pct}%")
print(f"Discount Amount: Rs.{discount_amount}")
print(f"Final Amount Payable: Rs.{final_amount}")
print("\nArmstrong numbers between 100 and 2000:", end=" ")
for num in range(100, 2001):
    temp = num
    digits = len(str(num))
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    if total == num:
        print(num, end=" ")
print()
n = int(input("\nEnter a number: "))
reversed_num = 0
temp = abs(n)
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
if n < 0:
    reversed_num = -reversed_num
print(f"Reversed number: {reversed_num}")
age = int(input("\nEnter age: "))
show_hour = int(input("Enter show time (24-hr format, e.g. 17 for 5 PM): "))
if age < 12:
    price = 5
elif age >= 60:
    price = 7
else:
    price = 10
if show_hour > 17:
    price += 2

print(f"Ticket price: ${price}")