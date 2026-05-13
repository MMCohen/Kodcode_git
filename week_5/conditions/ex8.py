num1, num2, num3 = int(input("please enter a first number: ")), int(input("please enter second a number: ")), int(input("please enter a third number: "))
acc_positive_numbers = (num1 > 0) + (num2 > 0) + (num3 > 0)
print(f"the number of positive numbers you entered is: {acc_positive_numbers}")