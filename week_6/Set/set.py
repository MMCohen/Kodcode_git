#qs1
def remove_duplicates(l: list):
    return list(set(l))

#qs2
def count_unique_elements(l: list):
    return sum(1 for _ in set(l))

#qs3
def common_elements(l1: list, l2: list):
    return sorted(set(l1) & set(l2)) # => return sorted(set(l1).intersection(l2))

#qs4
def elements_in_only_one(l1: list, l2: list):
    return sorted(set(l1).symmetric_difference(l2))

#qs5
def is_subset(a: list, b: list):
    return set(a).issubset(b)

#qs6
def unique_characters(s :str):
    # return len(set(s)) == len(s) # more Memory Complexity
    temp = set()
    for i in s:
        if i in temp:
            return False
        temp.add(i)
    return True

#qs7
def first_repeated_element(l: list):
    temp = set()
    for i in l:
        if i in temp:
            return i
        temp.add(i)
    return None

#qs8
def distinct_words(words: str):
    return len(set(words.lower().split()))

#qs9
def pair_sum_exists(l: list[int], target: int):
    s = set()
    for num in l:
        if target - num in s:
            return True
        s.add(num)
    return False

#qs10
def symmetric_difference(l1: list, l2: list):
    # return sorted({num: [*l1, *l2].count(num) for num in [*l1, *l2] if [*l1, *l2].count(num) == 1})
    result = []
    for num in l1:
        if not num in l2:
            result.append(num)
    for num in l2:
        if not num in l1:
            result.append(num)
    return sorted(result)


#qs1
assert remove_duplicates([1, 2, 2, 3, 1, 4, 3]) == [1, 2, 3, 4]
#qs2
assert count_unique_elements([1, 2, 2, 3, 1, 4]) == 4
#qs3
assert common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
#qs4
assert elements_in_only_one([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2, 5, 6]
#qs5
assert is_subset([1, 2, 3], [1, 2, 3, 4, 5]) == True
assert is_subset([1, 2, 6], [1, 2, 3, 4, 5]) == False
#qs6
assert unique_characters("abcdef") == True
assert unique_characters("hello") == False
#qs7
assert first_repeated_element([1, 2, 3, 2, 4, 1]) == 2
assert first_repeated_element([1, 2, 3, 4]) == None
#qs8
assert distinct_words("The cat and the dog and the bird") == 5
#qs9
assert pair_sum_exists([3, 1, 4, 7, 2], 6) == True
assert pair_sum_exists([3, 1, 4, 7, 2], 100) == False
#qs10
assert symmetric_difference([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2, 5, 6]




