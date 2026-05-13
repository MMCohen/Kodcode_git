user_age = int(input("please enter your age: "))

if user_age <= 0 or user_age >= 120:
    print("Invalid")
elif 0 < user_age <= 12:
    print("Child")
elif 13 <= user_age <= 17:
    print("Teen")
else:
    print("Adult")