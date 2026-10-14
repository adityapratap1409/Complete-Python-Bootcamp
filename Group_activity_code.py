import timeit

small_array = [12, -7, 0, 5, -18, 0, 23, -3, 8, 14, -1, 0, 9]


def benchmark_list_comprehension(nums):
    pos = len([x for x in nums if x > 0])
    neg = len([x for x in nums if x < 0])
    zero = len([x for x in nums if x == 0])
    even = len([x for x in nums if x % 2 == 0])
    odd = len([x for x in nums if x % 2 != 0])
    return pos, neg, zero, even, odd


def benchmark_sum_generator(nums):
    pos = sum(1 for x in nums if x > 0)
    neg = sum(1 for x in nums if x < 0)
    zero = sum(1 for x in nums if x == 0)
    even = sum(1 for x in nums if x % 2 == 0)
    odd = sum(1 for x in nums if x % 2 != 0)
    return pos, neg, zero, even, odd


def benchmark_dictionary_mapping(nums):
    counts = {"positive": 0, "negative": 0, "zero": 0, "even": 0, "odd": 0}
    for num in nums:
        sign = "positive" if num > 0 else ("negative" if num < 0 else "zero")
        parity = "even" if num % 2 == 0 else "odd"
        counts[sign] += 1
        counts[parity] += 1
    return counts


def benchmark_bitwise_operators(nums):
    even = odd = pos = neg = zero = 0
    for num in nums:
        if num & 1:
            odd += 1
        else:
            even += 1

        if num == 0:
            zero += 1
        elif num > 0:
            pos += 1
        else:
            neg += 1
    return pos, neg, zero, even, odd


print("Calculated Totals:")
print(f"List Comprehension: {benchmark_list_comprehension(small_array)}")
print(f"Sum Generator:       {benchmark_sum_generator(small_array)}")
print(f"Dictionary Mapping:  {benchmark_dictionary_mapping(small_array)}")
print(f"Bitwise Operators:   {benchmark_bitwise_operators(small_array)}\n")

runs = 100000

time_list_comp = timeit.timeit(
    lambda: benchmark_list_comprehension(small_array), number=runs
)
time_sum_gen = timeit.timeit(lambda: benchmark_sum_generator(small_array), number=runs)
time_dict_map = timeit.timeit(
    lambda: benchmark_dictionary_mapping(small_array), number=runs
)
time_bitwise = timeit.timeit(
    lambda: benchmark_bitwise_operators(small_array), number=runs
)

print("Execution Times:")
print(f"List Comprehension: {time_list_comp:.4f} seconds")
print(f"Sum Generator:       {time_sum_gen:.4f} seconds")
print(f"Dictionary Mapping:  {time_dict_map:.4f} seconds")
print(f"Bitwise Operators:   {time_bitwise:.4f} seconds")
