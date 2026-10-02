# Question 1

Data_X = set(["A", "R", "B", "C", "V", "K"])
Data_Y = set(["A", "D", "C", "Q", "R", "J"])

print("Data X:", Data_X)
print("Data Y:", Data_Y)

print("Union:", Data_X | Data_Y)
print("Intersection:", Data_X & Data_Y)
print("Difference X-Y:", Data_X - Data_Y)
print("Difference Y-X:", Data_Y - Data_X)
print("Symmetric Difference:", Data_X ^ Data_Y)


# Question 2


def count_numbers(numbers):
    pos = 0
    neg = 0

    for n in numbers:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1

    return {"Neg": neg, "Pos": pos}


numbers = [1, -2, 3, -4]

print(count_numbers(numbers))


# Question 3

hospital = {
    1: "Boy",
    2: "Girl",
    3: "Boy",
    4: "Girl",
    5: "Boy",
    6: "Girl",
    7: "Boy",
    8: "Boy",
    9: "Girl",
}

# One more girl is born
hospital[10] = "Girl"

boys = 0
girls = 0

for gender in hospital.values():
    if gender == "Boy":
        boys += 1
    else:
        girls += 1

print("Number of boys:", boys)
print("Number of girls:", girls)

# Searching for certificate number 10

if 10 in hospital:
    print("Certificate number 10:", hospital[10])
else:
    print("Not born in this hospital")

girl_list = []

for certificate, gender in hospital.items():
    if gender == "Girl":
        girl_list.append(certificate)

print("Girl child certificate numbers:", girl_list)


# Question 4

for i in range(1, 10):
    for j in range(2, 7):
        print(i + j)


# Modified program

for j in range(20, 25):
    for i in range(10):
        print(j)

# (q4-1)
# how many different values of j will be printed ?
# ANS = 5

# Q4-2
# How many times each j value will be printed?
# ANS = 9 TIMES

# Q4 - 3
for j in range(20, 25):
    for i in range(10):
        print(j)
