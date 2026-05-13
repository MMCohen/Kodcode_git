user_age = int(input("Please enter your age: "))
vip = input("Do you have VIP card [yes/no]: ")

if user_age < 16:
    print("automatically rejected!")
elif (user_age >= 18 and vip == "yes") or (19 <= user_age <= 21):
    print("access granted")
