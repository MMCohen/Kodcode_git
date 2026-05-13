user_input = input("Please enter one character: ")

if user_input < "A" or user_input > "z":
    print("Invalid")
else:
    if user_input in "aeiou":
        print("Vowel")
    else:
        print("Consonant")