4

# qs1
def safe_int(s):
    try:
        return int(s)
    except ValueError:
        return None


# qs2
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "undefined"


# qs3
def get_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "missing"


# qs4
def parse_ints(values):
    new_list = []
    for val in values:
        try:
            int(val)
        except ValueError as e:
            pass
        else:
            new_list.append(int(val))
    return new_list

# qs5
def set_age(age):
    if age < 0 or age > 150:
        raise ValueError
    return age


# qs6
def retry(func, n):
    for i in range(n):
        try:
            result = func()
            return result
        except Exception:
            if i == n - 1:
                raise


# qs7
def count_errors(funcs):
    counter = 0
    for func in funcs:
        try:
            func()
        except Exception:
            counter += 1
    return counter


# qs8
def load_config(path):
    try:
        with open(path, "r") as f:
            first_line = f.readline()
            int(first_line)
    except Exception as e:
        raise RuntimeError("failed to load config") from e

