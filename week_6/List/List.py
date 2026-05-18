#qs1
def sum_of_list(lst):
    acc = 0
    for i in lst:
        acc += i
    return acc

#qs2
def max_of_list(lst):
    max_num = lst[0]
    for i in lst:
        if i >  max_num:
            max_num = i
    return max_num

#qs3
def count_occurrences(lst, val):
    counter = 0
    for i in lst:
        if i == val:
            counter += 1
    return counter

#qs4
def reverse_a_list(lst):
    new_list = []
    for i in lst:
        new_list.insert(0, i)
    return new_list

#qs5
def remove_duplicates(lst):
    new_lst = []
    for i in lst:
        if not i in new_lst:
            new_lst.append(i)

#qs6
def second_largest(lst):
    new_lst = [i for i in lst if i != max(lst)]
    return max(new_lst) if new_lst else None

#qs7
def merge_two_sorted(lst_1, lst_2):
    i, j = 0, 0
    new_lst = []

    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] < lst_2[j]:
            new_lst.append(lst_1[i])
            i += 1
        else:
            new_lst.append(lst_2[j])
            j += 1

    new_lst.extend(lst_1[i:])
    new_lst.extend(lst_2[j:])

    return new_lst


#qs8
def rotate_a_list(lst, k):
    real_length = k % len(lst)
    return lst[-real_length::] + lst[:-real_length]

l =[1,2,3,4,5]
print(l)
st = 0
en = 4
while st < en:
    l[st], l[en]= l[en],l[st]
    st +=1
    en -=1
print(l)
