import array as A

my_array = A.array("i", [11, 21, 31, 41])
my_array.extend(A.array("i", [50, 60, 70]))
print("Extended array:", my_array)
# With dynamic input
# user_input=eval(input("enter List:"))
# print(user_input)
# With List function
l = __builtins__.list(range(0, 10, 2))
print(l)
n1 = [1, 8, 4, 100, "25", "hello", "ram"]
n1_str = [str(x) for x in n1]
n1_str.sort()
print(n1_str)
num = 255

binary_val = bin(num)[2:]
octal_val = oct(num)[2:]
hex_val = hex(num)[2:].upper()

print(f"Decimal: {num}")
print(f"Binary: {binary_val}")
print(f"Octal: {octal_val}")
print(f"Hexadecimal: {hex_val}")
# Example Input list: [101, 102, 101, 103, 102, 101]
items_input = input("Enter product IDs separated by spaces: ").split()

# a) Store product IDs in a list
product_ids = [int(x) for x in items_input]

# b) & c) Count and display frequency of each product ID
freq_dict = {}
for pid in product_ids:
    freq_dict[pid] = freq_dict.get(pid, 0) + 1

print("\nProduct ID Frequencies:")
for pid, count in freq_dict.items():
    times_str = "time" if count == 1 else "times"
    print(f"{pid} -> {count} {times_str}")
