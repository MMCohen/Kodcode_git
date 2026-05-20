#qs2
def make_counter():
    num = 0
    
    def counter():
        nonlocal num
        num += 1
        return num

    return counter

c = make_counter()
print(c())
print(c())
print(c())
