
#qs9
"""
before:
def add_item(item, bag=[]):
    bag.append(item)
    return bag
    """

def add_item(item, bag=None):
    if bag is None:
        bag = []

    bag.append(item)
    return bag

print(add_item(1))
print(add_item(2))
print(add_item(3))