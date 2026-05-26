

#qs1
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return self.name + " says woof"

#qs2
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width

#qs3
class Counter:
    def __init__(self, count = 0):
        self.count = count

    def increment(self):
        self.count += 1

    def value(self):
        return self.count

#qs4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return str((self.x, self.y))

#qs5
class BankAccount:
    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("deposit must be positive!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("you dont have enough money!")

#qs6
class Temperature:
    def __init__(self, temperature):
        self.celsius_temperature = temperature

    def to_fahrenheit(self):
        return self.celsius_temperature * 1.8 + 32

#qs7
class Student:
    def __init__(self, name: str):
        self.name: str = name
        self.school: str = "Kodcode"

#qs8
class Player:
    player_count = 0
    def __init__(self):
        self.name = None
        Player.player_count += 1

#qs9
class Money:
    def __init__(self, amount: int = 0):
        self.amount: int = amount

    def is_more_than(self, other_instance: Money):
        return self.amount > other_instance.amount

#qs10
class Playlist:
    def __init__(self):
        self.stored_title = []

    def add(self, title):
        self.stored_title.append(title)

    def remove(self, title):
        self.stored_title.remove(title)

    def count(self):
        return len(self.stored_title)

    def __str__(self):
        return str(self.stored_title)

# #qs1
# dog1 = Dog("Rex")
# print(dog1.bark())
# #qs2
# r1 = Rectangle(5,3)
# print(r1.area())
# #qs3
# c1 = Counter()
# c1.increment()
# c1.increment()
# print(c1.value())
# #qs4
# print(Point(1,2)) # -> (1, 2)
# #qs5
# ba1 = BankAccount()
# ba1.deposit(100)
# ba1.withdraw(150)
# ba1.withdraw(70)
# print(ba1.balance)
# #qs6
# print(Temperature(100).to_fahrenheit())
# #qs7
# s1 = Student("Moshe")
# s2 = Student("Menachem")
# print(f"{s1.name = }, {s2.name =}")
# s1.name = "Moshe Shmuel"
# print(f"{s1.name = }, {s2.name =}")
# #qs8
# print(Player.player_count)
# p1, p2, p3 = Player(), Player(), Player()
# print(Player.player_count)
# #qs9
# m1 = Money(100)
# m2 = Money(200)
# print(m2.is_more_than(m1))
# #qs10
# pl1 = Playlist()
# print(pl1)
# pl1.add("Nice")
# pl1.add("Dance")
# pl1.add("Chazanut")
# print(pl1)
# pl1.remove("Dance")
# print(pl1)
