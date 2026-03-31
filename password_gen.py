import random
import string

def pass_gen_mod(pass_len, letters, digits, punctuation, amount_of_gen_pass):
    characters = ""
    if not letters and not digits and not punctuation:
        print("No character types selected!")
        return
    
    if letters:
        letters = string.ascii_letters
    else:
        letters = ""
    if digits:
        digits = string.digits
    else:
        digits = ""
    if punctuation:
        punct = string.punctuation
    else:
        punct = ""

    characters = letters + digits + punct

    for i in range(amount_of_gen_pass):
        password = ""
        for j in range(pass_len):
            password += random.choice(characters)
        print(f"Your generated password: {password}")
    

def pass_gen_def():
    characters = string.ascii_letters + string.digits
    pass_len = 8
    password = ""
    for i in range(pass_len):
        password += random.choice(characters)

    print(f"Your generated password: {password}")


pass_len = 8
allow_letters = True
allow_digits = True
allow_punct = False
amount_of_gen_pass = 1

while True:
    print(f"\n{"=" * 5}Password Generator{"=" * 5}")
    print("Select what you want to do: ")
    print("1. Modify password generator")
    print("2. Generate password default settings")
    print("3. Exit")

    choice = int(input("Enter your choice pick (number): "))
    if choice == 1:
        while True:
            print(f"\n{"=" * 5}Password Generator Modifier{"=" * 5}")
            print("1. Set password lenght (default = 8)")
            print("2. Allow letters (default = True)")
            print("3. Allow digits (default = True)")
            print("4. Allow punctuation (default = False)")
            print("5. Amount of passwords (default = 1)")
            print("6. Generate password/s")
            print("7. Go back")

            pick = int(input("Enter what you want to edit (number): "))


            if pick == 1:
                pass_len = int(input("Enter password lenght: "))
            elif pick == 2:
                allow_letters = input("Allow letters (y/n): ").lower() == "y"
            elif pick == 3:
                allow_digits = input("Allow digits (y/n): ").lower() == "y"
            elif pick == 4:
                allow_punct = input("Allow punctuation (y/n): ").lower() == "y"
            elif pick == 5:
                amount_of_gen_pass = int(input("Input amount of passwords you want to be generated: "))
            elif pick == 6:
                pass_gen_mod(pass_len, allow_letters, allow_digits, allow_punct, amount_of_gen_pass)
            elif pick == 7:
                break
            else:
                print("Incorrect choice pick.")

    elif choice == 2:
        pass_gen_def()
    elif choice == 3:
        break
    else:
        print("Incorrect choice pick.")


