# ==============================================================================
# CSE1021 - OPEN BOOK EXAM SOLUTIONS
# Single Continuous Script (Ready for VS Code)
# ==============================================================================


# ==============================================================================
# QUESTION 1
# ==============================================================================
print("=" * 60)
print("QUESTION 1")
print("=" * 60)

"""
--- Q1(a.1) IDENTIFICATION OF ERRORS & ITERATION TRACE ---
Original Code:
    marks = [72, 65, 80, 58, 91, 60]
    swaps = 0
    total = 0
    for i in range(len(marks)):
        if marks[i] > marks[i+1]:
            marks[i] = marks[i+1]
            marks[i+1] = marks[i]
            swaps += 1
        total = total + marks[i]
    print(swaps, total)

Errors Identified:
1. Line 5 (`if marks[i] > marks[i+1]:`):
   - Causes `IndexError: list index out of range` when i = 5 (len(marks) - 1), because `marks[i+1]` tries to access index 6.
   - Fix: Loop range should be `range(len(marks) - 1)`.

2. Lines 6–7 (`marks[i] = marks[i+1]` and `marks[i+1] = marks[i]`):
   - Logical error. Overwrites `marks[i]` before saving its original value. Both positions become identical, permanently losing data.
   - Fix: Use Python tuple swapping: `marks[i], marks[i+1] = marks[i+1], marks[i]`.

3. Line 9 (`total = total + marks[i]`):
   - Logical error. Summing inside a loop running `len(marks)-1` times misses the last element (`marks[-1]`). If elements swap before addition, updated values are summed instead of originals.

Trace until program crashes with IndexError:
  Initial: marks = [72, 65, 80, 58, 91, 60], swaps = 0, total = 0
  - Iteration 0 (i=0): 72 > 65 True -> marks=[65, 65, 80, 58, 91, 60], swaps=1, total=65
  - Iteration 1 (i=1): 65 > 80 False -> total = 65 + 65 = 130
  - Iteration 2 (i=2): 80 > 58 True -> marks=[65, 65, 58, 58, 91, 60], swaps=2, total=130+58 = 188
  - Iteration 3 (i=3): 58 > 91 False -> total = 188 + 58 = 246
  - Iteration 4 (i=4): 91 > 60 True -> marks=[65, 65, 58, 58, 60, 60], swaps=3, total=246+60 = 306
  - Iteration 5 (i=5): Evaluates `marks[5] > marks[6]` -> Program Crashes with IndexError!

--- Q1(a.2) EVALUATION OF STUDENT'S CLAIM ---
- The claim is CORRECT. Swapping elements reorders them but keeps the overall set of numbers unchanged, so the sum remains constant ($\sum marks$).
- Summing before the loop via `total = sum(marks)` is faster, mathematically accurate, and avoids boundary/swapping side-effects inside the loop.
"""

# Continuous Corrected Code for Q1:
marks = [72, 65, 80, 58, 91, 60]
swaps = 0
total = sum(marks)  # Pre-summing as elements remain identical

for i in range(len(marks) - 1):
    if marks[i] > marks[i+1]:
        marks[i], marks[i+1] = marks[i+1], marks[i]  # Correct swap
        swaps += 1

print(f"Corrected Swaps: {swaps}")
print(f"Corrected Total Sum: {total}")
print(f"List after 1 pass: {marks}\n")


# ==============================================================================
# QUESTION 2
# ==============================================================================
print("=" * 60)
print("QUESTION 2")
print("=" * 60)

"""
--- Q2(a) TRACE OF fib(5) AND EXPLANATION OF BUG ---
Trace for fib(5) using original code:
  Initial: a = 0, b = 1
  i = 0: a = 1, b = 1 + 1 = 2
  i = 1: a = 2, b = 2 + 2 = 4
  i = 2: a = 4, b = 4 + 4 = 8
  i = 3: a = 8, b = 8 + 8 = 16
  i = 4: a = 16, b = 16 + 16 = 32
  Returns: 16 (Incorrect! F(5) should be 5).

Why it is wrong:
  Because `a = b` runs first, `a` loses its old value. When `b = a + b` runs, it calculates `b = b + b = 2 * b`, doubling `b` each time instead of adding the two distinct preceding terms.

Fix: Use simultaneous assignment `a, b = b, a + b`.
"""

# Q2(b) Continuous execution & evaluation of claim "F(3n) > n!"
print(f"{'n':<5}{'F(3n)':<12}{'n!':<12}{'F(3n) > n!':<10}")
print("-" * 40)

for n in range(1, 11):
    # Calculate F(3n) continuously
    a, b = 0, 1
    for _ in range(3 * n):
        a, b = b, a + b
    f_3n = a

    # Calculate n! continuously
    fact_n = 1
    for i in range(1, n + 1):
        fact_n *= i

    print(f"{n:<5}{f_3n:<12}{fact_n:<12}{str(f_3n > fact_n):<10}")

"""
Justification for Q2(b):
  The claim "F(3n) > n!" is FALSE for n >= 9.
  - Fibonacci numbers grow exponentially: F(3n) grows at a rate of (phi^3)^n ≈ (4.236)^n.
  - Factorials n! grow super-exponentially. Once n > 4.236 (specifically at n = 9), the factor (n+1) multiplied in each step exceeds 4.236, causing n! to permanently outgrow F(3n).
"""
print()


# ==============================================================================
# QUESTION 3
# ==============================================================================
print("=" * 60)
print("QUESTION 3")
print("=" * 60)

"""
--- Q3(a) INDEX ROLES & JUSTIFICATION ---
Roles of indices:
- `low`: Points to the right boundary of elements < P.
- `mid`: Points to the current element being evaluated.
- `high`: Points to the left boundary of elements > P.

Why `mid` MUST NOT be advanced after swapping with `high`:
  The element swapped from `high` to `mid` has NOT been inspected yet. If `mid` were advanced immediately, this unexamined element would be skipped, resulting in an unsorted/unpartitioned list.
"""

readings = [9, 4, 7, 4, 12, 1, 7, 4]
P = 7

low = 0
mid = 0
high = len(readings) - 1

print("Q3 Iteration Trace:")
print(f"Initial: low={low}, mid={mid}, high={high}, list={readings}")

iter_count = 1
while mid <= high:
    if readings[mid] < P:
        readings[low], readings[mid] = readings[mid], readings[low]
        low += 1
        mid += 1
    elif readings[mid] == P:
        mid += 1
    else:  # readings[mid] > P
        readings[mid], readings[high] = readings[high], readings[mid]
        high -= 1
        # mid is not advanced here
    
    print(f"Iter {iter_count:2d}: low={low}, mid={mid}, high={high}, list={readings}")
    iter_count += 1

print(f"\nFinal Partitioned List: {readings}\n")


# ==============================================================================
# QUESTION 4
# ==============================================================================
print("=" * 60)
print("QUESTION 4")
print("=" * 60)

#(a) Function explicitly requested in Question 4(a)
def reverse_part(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# --- Continuous Execution for Q4(b) and Q4(c) ---
# Demonstration for k = 3
data = [10, 20, 30, 40, 50, 60, 70]
n = len(data)
k = 3

print(f"Original list (k={k}): {data}")

# 1. Reverse entire array
reverse_part(data, 0, n - 1)
print(f"After Reversal 1 (0 to {n-1}):   {data}")

# 2. Reverse first k elements
reverse_part(data, 0, k - 1)
print(f"After Reversal 2 (0 to {k-1}):   {data}")

# 3. Reverse remaining n-k elements
reverse_part(data, k, n - 1)
print(f"After Reversal 3 ({k} to {n-1}):   {data}\n")

"""
Justification for Q4(b):
  Dividing array into [X | Y] where Y is the last k elements:
  1. Reversing whole array yields [Y^R | X^R].
  2. Reversing first k elements yields [Y | X^R].
  3. Reversing remaining (n-k) elements yields [Y | X] (Right rotation achieved).
"""

# Demonstration for k = 10
data_k10 = [10, 20, 30, 40, 50, 60, 70]
n = len(data_k10)
k = 10
effective_k = k % n  # Handles k > len(data)

reverse_part(data_k10, 0, n - 1)
reverse_part(data_k10, 0, effective_k - 1)
reverse_part(data_k10, effective_k, n - 1)

print(f"Final List for k=10 (Effective k={effective_k}): {data_k10}")