

# qs 1
def is_even(n):
    return n % 2 == 0


# qs 2
def factorial(n):
    num = 1
    acc = 1
    while num <= n:
        acc = acc * num
        num += 1
    return acc


# qs3
def digital_root(n):
    """the question is empty"""
    pass


# qs4
def is_palindrome(s):
    num = s
    new_num = int()
    while num:
        new_num *= 10
        new_num += num % 10
        num = num // 10
    return new_num == s


# qs5
def sums_digits(n):
    """repeatedly sums its digits until the result is a single digit (0-9).
        Return that digit."""
    num = n
    while num > 9:
        acc = 0
        while num:
            acc += num % 10
            num = num // 10
        num = acc
    return num


# qs6
def count_digits(n):
    num = n
    cnt = 0
    while num:
        cnt += 1
        num = num // 10

    return cnt


# qs7
def reverse_integer(s):
    num = s
    new_num = int()
    while num:
        new_num *= 10
        new_num += num % 10
        num = num // 10
    return new_num


# qs8
def move_zeros_to_end(lst: list):
    new_lst = lst.copy()
    idx_of_zeros = []

    for i, num in enumerate(new_lst):
        if num == 0:
            idx_of_zeros.insert(0, i)
    for i in idx_of_zeros:
        temp = new_lst.pop(i)
        new_lst.append(temp)
    return new_lst


# qs9
def sum_average_minimum_maximum(lst):
    return sum(lst), sum(lst) / len(lst), min(lst), max(lst)


# qs10
def reverse_a_list(lst: list):
    return lst[::-1]


# qs11
def removes_duplicates(lst: list):
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)
    return new_lst





############################### testing ##################################
assert is_even(9) == False
assert is_even(8) == True

assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720

assert is_palindrome(576788) == False
assert is_palindrome(123321) == True
assert is_palindrome(12321) == True

assert sums_digits(479) == 2
assert sums_digits(9539) == 8

assert count_digits(4) == 1
assert count_digits(386) == 3
assert count_digits(10000) == 5

assert reverse_integer(1200) == 21
assert reverse_integer(968) == 869
assert reverse_integer(253) == 352

assert move_zeros_to_end([4, 0, 7, 2, 0, 9, 1, 5]) == [4, 7, 2, 9, 1, 5, 0, 0]
assert move_zeros_to_end([1, 0, 2, 0, 3]) == [1,2,3,0,0]

assert sum_average_minimum_maximum([4, 7, 2, 9, 1, 5]) == (28, 4.666666666666667, 1, 9)

assert removes_duplicates([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [3, 1, 4, 5, 9, 2, 6]