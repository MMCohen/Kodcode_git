#qs 1
def sum_tpl(tpl: tuple):
    acc = 0
    for i in tpl:
        acc += i
    return acc

#qs2
def max_tpl(tpl):
    max_num = tpl[0]

    for i in tpl:
        if i > max_num:
            max_num = i

    return max_num

#qs3
def count_occurrences(tpl, val):
    cnt = 0
    for i in tpl:
        if i == val:
            cnt += 1
    return cnt

#qs4
def reverse_a_tuple(tpl):
    new_lst = []
    for i in range(len(tpl)-1,-1,-1):
        new_lst.append(tpl[i])
    return tuple(new_lst)

#qs5
def swap_pairs(tpl):
    temp_list = list(tpl)
    for i in range(0, len(temp_list), 2):
        temp_list[i], temp_list[i+1] = temp_list[i+1], temp_list[i]
    return tuple(temp_list)

#qs6
def min_and_max(tpl):
    min_num = tpl[0]
    max_num = tpl[0]
    for i in tpl:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    return min_num, max_num

#qs7
def distance(point_1, point_2):
    return ((point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2) ** 0.5

#qs8
def merge_and_sort(tuple_1, tuple_2):
    return tuple(sorted(tuple_1 + tuple_2))

#qs9
def frequency_table(tpl):
    frequency_dict = dict()
    for i in tpl:
        frequency_dict[i] = frequency_dict.get(i, 0) + 1
    return tuple(frequency_dict.items())

#qs10
def rotate_a_tuple(tpl: tuple, k: int):
    if tpl:
        k = k % len(tpl)
    return tpl[-k:] + tpl[:-k]




#qs1
assert sum_tpl((1, 2, 3, 4, 5)) == 15
#qs2
assert max_tpl((3, 7, 2, 8, 5)) == 8
#qs3
assert count_occurrences((1, 2, 3, 2, 4, 2), 2) == 3
#qs4
assert reverse_a_tuple((1, 2, 3, 4)) == (4, 3, 2, 1)
#qs5
assert swap_pairs((1, 2, 3, 4, 5, 6)) == (2, 1, 4, 3, 6, 5)
#qs6
assert min_and_max((4, 1, 7, 3, 5)) == (1,7)
#qs7
assert distance((0, 0), (3, 4)) == 5.0
#qs8
assert merge_and_sort((3, 1, 4), (1, 5, 9)) == (1, 1, 3, 4, 5, 9)
#qs9
assert frequency_table(("a", "b", "a", "c", "b", "a")) == (("a", 3), ("b", 2), ("c", 1))
#qs10
assert rotate_a_tuple((1, 2, 3, 4, 5), 7) == (4, 5, 1, 2, 3)