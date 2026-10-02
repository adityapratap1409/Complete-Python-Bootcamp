# (QUESTION 1)

# (a) One compare-and-exchange pass over a list of marks
# The program exchanges neighbouring marks if the left mark is larger,
# counts how many exchanges were made, and finds the sum of all marks.

marks = [72, 65, 80, 58, 91, 60]
swaps = 0
total = 0

# (a.1) Corrected logic with tracing and error identification
# Original errors:
# 1. range(len(marks)) causes IndexErFror when i = last index (marks[i+1] invalid)
# 2. Swapping logic was wrong — both elements became equal.
# 3. Summation inside loop is fine but should be done after the loop for clarity.

for i in range(len(marks) - 1):  # fix: stop before last index
    if marks[i] > marks[i + 1]:
        # correct swap
        temp = marks[i]
        marks[i] = marks[i + 1]
        marks[i + 1] = temp
        swaps += 1
    # tracing each iteration
    print(f"After iteration {i}: marks = {marks}, swaps = {swaps}")

# summation after one pass
for i in range(len(marks)):
    total += marks[i]

print("\nFinal marks list:", marks)
print("Total swaps:", swaps)
print("Sum of marks:", total)

# (a.2) Evaluation of student's claim
# The student is correct: exchanging values does not change the sum of the list.
# Therefore, the summation can be done once before the loop.
# However, summing inside the loop still gives the same result if done correctly.

# Demonstration:
total_before = sum(marks)
print("\nSum before loop (unchanged by swaps):", total_before)


# Question 2: Comparing factorial growth and Fibonacci sequence

# (a) Trace fib(5), explain the error, and correct the function
# Original function:
# def fib(n):
#     a, b = 0, 1
#     for i in range(n):
#         a = b
#         b = a + b
#     return a
# Problem: 'a' is updated before using its old value, so the previous 'a' is lost.
# Corrected version (same loop structure, no recursion or list):


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b  # simultaneous update keeps old 'a' value
        print(f"Iteration {i+1}: a = {a}, b = {b}")  # tracing each iteration
    return a


# Trace fib(5)
print("\nTracing fib(5):")
result = fib(5)
print("\nReturned value:", result)

# Explanation of trace:
# i=1 → a=1, b=1
# i=2 → a=1, b=2
# i=3 → a=2, b=3
# i=4 → a=3, b=5
# i=5 → a=5, b=8
# So fib(5) = 5, which is correct.

# (b) Evaluate the claim “F(3n) is always greater than n!”
# Compare Fibonacci and factorial growth for small n

import math

print("\nEvaluating F(3n) vs n! for n = 1 to 6:")
for n in range(1, 7):
    fib_val = fib(3 * n)
    fact_val = math.factorial(n)
    print(
        f"n = {n}, F(3n) = {fib_val}, n! = {fact_val}, F(3n) > n! → {fib_val > fact_val}"
    )

# Discussion:
# Fibonacci grows exponentially (≈ φⁿ / √5), while factorial grows faster (super‑exponential).
# For small n, F(3n) may exceed n!, but as n increases, factorial growth quickly overtakes Fibonacci.
# Therefore, the difference does NOT widen in favor of Fibonacci — factorial dominates for large n.


# Question 3: Partitioning diameters using three indices (low, mid, high)
# Parts smaller than P → front
# Parts equal to P → middle
# Parts larger than P → end
# Done in place, single pass, no extra list.

readings = [9, 4, 7, 4, 12, 1, 7, 4]
P = 7

# (a) Program using low, mid, high
# Roles:
# low → boundary for elements < P
# mid → current element under examination
# high → boundary for elements > P
# mid is NOT advanced after swapping with high because the new element at mid
# must be checked again (it may belong to another category).

low, mid, high = 0, 0, len(readings) - 1

while mid <= high:
    if readings[mid] < P:
        readings[low], readings[mid] = readings[mid], readings[low]
        low += 1
        mid += 1
    elif readings[mid] == P:
        mid += 1
    else:
        readings[mid], readings[high] = readings[high], readings[mid]
        high -= 1
    print(f"Iteration: low={low}, mid={mid}, high={high}, readings={readings}")

print("\nFinal partitioned list:", readings)
# Question 4: Rotate list right by k positions using reversal technique
# No slicing, no extra list, no reverse(), reversed(), or insert().
data = [10, 20, 30, 40, 50, 60, 70]


# (a) Function to reverse part of list in place
def reverse_part(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# (b) Rotate right by k positions using three reversals
def rotate_right(arr, k):
    n = len(arr)
    k = k % n  # handle k > n
    print(f"\nOriginal list: {arr}")

    # Step 1: Reverse entire list
    reverse_part(arr, 0, n - 1)
    print(f"After first reversal: {arr}")

    # Step 2: Reverse first k elements
    reverse_part(arr, 0, k - 1)
    print(f"After second reversal (first {k} elements): {arr}")

    # Step 3: Reverse remaining elements
    reverse_part(arr, k, n - 1)
    print(f"After third reversal (remaining elements): {arr}")

    return arr


# (c) Show results for k = 3 and k = 10
print("\nRotation for k = 3:")
rotated_3 = rotate_right(data.copy(), 3)
print("\nRotation for k = 10:")
rotated_10 = rotate_right(data.copy(), 10)
