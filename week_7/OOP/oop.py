""" """
"""
1. What is the difference between a class and an object? Give a real-world analogy.

2. What does self refer to, and why is it the first parameter of every instance method?

3. When does __init__ run? What is its job?

4. What is the difference between an instance attribute and a class attribute? When is each shared
between objects?

5. Why can you call dog.bark() without passing an argument for self ?

6. What does the following code print, and why?
"""
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"
d = Dog("Rex")
print(d.speak())

"""
7. What is the difference between __str__ and __repr__ ? Which one does print() use?

8. What does the following code print? Explain what __str__ changes.
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"
p = Point(2, 3)
print(p)
"""
9. What is the bug in the following code? How would you fix it?
        """
class Counter:
    def __init__(self):
        count = 0
    def increment(self):
        self.count += 1
"""        
10. What is the difference between type(obj) and isinstance(obj, Cls) ? When would you
prefer each?

11. Why does accessing obj.color raise an AttributeError if color was never assigned? How
can you avoid it?

12. What does the following code print? Walk through each step.
"""
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        self.balance -= amount

acc = BankAccount(100)
acc.deposit(50)
acc.withdraw(30)
print(acc.balance)

"""
13. Why is it better to keep data and the functions that use it together in a class rather than as
separate global variables and functions?

14. What does the following code print, and why does changing c1 not change c2 ?
"""
class Color:
    def __init__(self, name):
        self.name = name
c1 = Color("red")
c2 = Color("blue")
c1.name = "green"
print(c1.name, c2.name)