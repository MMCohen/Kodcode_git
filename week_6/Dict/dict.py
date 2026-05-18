#qs1
def sum_of_values(d: dict):
    acc = 0
    for i in d.values():
        acc += i
    return acc

#qs2
def key_with_maximum(d: dict):
    max_key = int()
    max_val = int()
    for k, v in d.items():
        if v > max_val:
            max_key = k
            max_val = v
    return max_key

#qs3
def count_characters(s: str):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d

#qs4
def invert_a_dictionary(d: dict):
    return {v: k for k, v in d.items()}

#qs5
def merge_two_dictionaries(d1: dict, d2: dict):
    d1.update(d2)
    return d1

#qs6
def filter_by_value(d: dict, threshold: int):
    return {k: v for k, v in d.items() if v > threshold}

#qs7
def group_by_first_letter(lst: list[str]):
    d = {}
    for word in lst:
        d[word[0]] = d.get(word[0], []) + [word]
    return d

#qs8
def word_frequency(words: str):
    d = {}
    for word in words.split():
        d[word] = d.get(word, 0) + 1

    return d

#qs9
def common_keys(d1: dict, d2: dict):
    return sorted(key for key in d1 if key in d2)

#qs10
def most_frequent_value(d: dict):
    return max(d.values(), key= lambda x: [d.values()].count(x))


#qs1
assert sum_of_values({"a": 1, "b": 2, "c": 3}) == 6
#qs2
assert key_with_maximum({"a": 3, "b": 7, "c": 5}) == "b"
#qs3
assert count_characters("banana") == {"b": 1, "a": 3, "n": 2}
#qs4
assert invert_a_dictionary({"a": 1, "b": 2, "c": 3}) == {1: "a", 2: "b", 3: "c"}
#qs5
assert merge_two_dictionaries({"a": 1, "b": 2}, {"b": 20, "c": 30}) == {"a": 1, "b": 20, "c": 30}
#qs6
assert filter_by_value({"a": 1, "b": 5, "c": 3, "d": 8}, 3) == {"b": 5, "d": 8}
#qs7
assert group_by_first_letter(["apple", "ant", "banana", "berry", "cherry"]) == {"a": ["apple", "ant"], "b": ["banana", "berry"], "c": ["cherry"]}
#qs8
assert word_frequency("the cat sat on the mat") == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}
#qs9
assert common_keys({"a": 1, "b": 2, "c": 3}, {"b": 9, "c": 8, "d": 7}) == ["b", "c"]
#qs10
assert most_frequent_value({"a": 1, "b": 2, "c": 1, "d": 3, "e": 1}) == 1