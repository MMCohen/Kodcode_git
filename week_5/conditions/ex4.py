saved_password = "123456"
user_password = input("please enter a password: ")

if user_password == saved_password:
    print("Access Granted")
elif len(user_password) < 8:
    print("too short!")
else:
    print("wrong password")
