import random
from time import sleep

print("Welcome to PassMate!")
print("What would you like to do today?")
select = input("1. Generate a Password.(PRESS 1)\n2. Play PassBuilt Game.(PRESS 2)\n3. Exit. (PRESS 3)\n")
#NUMERIC PASSWORD
def numeric_pass():
    numb = "1234567890"
    num_shuff = list(numb)
    random.shuffle(num_shuff)
    main_numpass = "".join(num_shuff[:n])
    print("Your NUMERIC PASSWORD is: ",main_numpass)

#ALPHABETIC PASSWORD
def alpha_pass():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c_alphabet = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    alpha_shuff = list(alphabet)
    alpha_shuff1 = list(c_alphabet)
    random.shuffle(alpha_shuff)
    random.shuffle(alpha_shuff1)
    main_alphapass = "".join(alpha_shuff[:6])
    main_ualphapass = "".join(alpha_shuff1[:6])
    inp1 = input("Select a type for your PASSWORD:\nUPPERCASE/LOWERCASE/MIXED\n")
    if inp1.upper() == "UPPERCASE" or inp1 == "1":
        print("Your UPPERCASE PASSWORD is: ", main_ualphapass)
    elif inp1.upper() == "LOWERCASE" or inp1 == "2":
        print("Your LOWERCASE PASSWORD is: ", main_alphapass)
    elif inp1.upper() == "MIXED" or inp1 == "3":
        mixed = main_alphapass + main_ualphapass
        mixed_demo = list(mixed)
        random.shuffle(mixed_demo)
        mixed_aplhapass = "".join(mixed_demo[:n])
        print("Your MIXED PASSWORD is: ", mixed_aplhapass)
    else:
        print("Invalid choice")

#ALPHANUMERIC PASSWORD
def alphanum_pass():
    numb = "1234567890"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c_alphabet = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    alphanum_pass = list(numb + alphabet + c_alphabet)
    random.shuffle(alphanum_pass)
    main_alphanumpass = "".join(alphanum_pass[:n])
    print("Your ALPHANUMERIC PASSWORD is: ", main_alphanumpass)

#COMPLEX PASSWORD
def complex_pass():
    numb = "1234567890"
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    c_alphabet = "ABCDEFGHIJLMNOPQRSTUVWXYZ"
    symb = "!#$%&'()*+,-.:;<=>?@[]^_`{|}~"
    comp_pass = list(numb + alphabet + c_alphabet + symb)
    random.shuffle(comp_pass)
    main_comppass = "".join(comp_pass[:n])
    print("Your COMPLEX PASSWORD is: ", main_comppass)

#PASSPHRASES PASSWORD
def passphrases():
    passphrases = "correct", "horse", "battery", "staple", "umbrella", "garden", "table", "cloud", "river", "mountain", "coffee", "moonlight", "wizard", "bicycle", "dragon", "star", "ocean", "whisper", "echo", "forest", "sunflower", "keyboard", "pizza", "rainbow"
    phrasesp_pass = list(passphrases)
    random.shuffle(phrasesp_pass)
    main_phrasepass = "".join(phrasesp_pass[:n])
    print("Your PASSPHRASES PASSWORD is: ", main_phrasepass)

if select == "1":
    print("Welcome to PassGen!")
    print("---GENERATE A NEW PASSWORD---")
    n = int(input("Enter the desired PASSWORD length: "))
    while True:
        if n < 3:
            print("the PASSWORD'S length must be at least 3")
            n = int(input("Enter the desired PASSWORD length: "))
        else:
            pass_type = input("Enter the type of PASSWORD you want to generate\n1. Numeric Password.(PRESS 1)\n2. Alphabetic Password.(PRESS 2)\n" \
            "3. Alphanumeric Password.(PRESS 3)\n4. Complex Password\n5. Passphrases Password.(PRESS 4)\n")
            while True:
                if pass_type == "1":
                    print("Here is your NUMERIC PASSWORD:")
                    numeric_pass()
                    agree = input("1. ACCEPT\n2. CHANGE\n")
                    while True:
                        if agree == "1" or agree.upper() == "ACCEPT":
                            print("---THANK YOU FOR USING PASSGEN---")
                            quit()
                        elif agree == "2" or agree.upper() == "CHANGE":
                            print("Changing the password...")
                            sleep(1)
                            numeric_pass()
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                        else:
                            print("Invalid choice. Please select 1 to ACCEPT or 2 to CHANGE.")
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                elif pass_type == "2":
                    print("Here is your ALPHABETIC PASSWORD:")
                    alpha_pass()
                    agree = input("1. ACCEPT\n2. CHANGE\n")
                    while True:
                        if agree == "1" or agree.upper() == "ACCEPT":
                            print("---THANK YOU FOR USING PASSGEN---")
                            quit()
                        elif agree == "2" or agree.upper() == "CHANGE":
                            print("Changing the password...")
                            sleep(1)
                            alpha_pass()
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                        else:
                            print("Invalid choice. Please select 1 to ACCEPT or 2 to CHANGE.")
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                elif pass_type == "3":
                    print("Here is your ALPHANUMERIC PASSWORD:")
                    alphanum_pass()
                    agree = input("1. ACCEPT\n2. CHANGE\n")
                    while True:
                        if agree == "1" or agree.upper() == "ACCEPT":
                            print("---THANK YOU FOR USING PASSGEN---")
                            quit()
                        elif agree == "2" or agree.upper() == "CHANGE":
                            print("Changing the password...")
                            sleep(1)
                            alphanum_pass()
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                        else:
                            print("Invalid choice. Please select 1 to ACCEPT or 2 to CHANGE.")
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                elif pass_type == "4":
                    print("Here is your COMPLEX PASSWORD:")
                    complex_pass()
                    agree = input("1. ACCEPT\n2. CHANGE\n")
                    while True:
                        if agree == "1" or agree.upper() == "ACCEPT":
                            print("---THANK YOU FOR USING PASSGEN---")
                            quit()
                        elif agree == "2" or agree.upper() == "CHANGE":
                            print("Changing the password...")
                            sleep(1)
                            complex_pass()
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                        else:
                            print("Invalid choice. Please select 1 to ACCEPT or 2 to CHANGE.")
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                elif pass_type == "5":
                    print("Here is your PASSPHRASES PASSWORD:")
                    passphrases()
                    agree = input("1. ACCEPT\n2. CHANGE\n")
                    while True:
                        if agree == "1" or agree.upper() == "ACCEPT":
                            print("---THANK YOU FOR USING PASSGEN---")
                            quit()
                        elif agree == "2" or agree.upper() == "CHANGE":
                            print("Changing the password...")
                            sleep(1)
                            passphrases()
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                        else:
                            print("Invalid choice. Please select 1 to ACCEPT or 2 to CHANGE.")
                            agree = input("1. ACCEPT\n2. CHANGE\n")
                else:
                    print("INVALID CHOICE")
                    pass_type = input("Enter the type of PASSWORD you want to generate\n1. Numeric Password.(PRESS 1)\n2. Alphabetic Password.(PRESS 2)\n" \
                    "3. Alphanumeric Password.(PRESS 3)\n4. Complex Password\n5. Passphrases Password.(PRESS 4)\n")
elif select == "2":
    print("Welcome to PassBuilt!")
    print("---BUILT PASSWORD GAME---")
    print("LEVEL 1")
    print("RULE:\n1.At least 3 characters long.")
    code = input("Write a Password: ")
    if len(code) >= 3:
        print("PASSWORD ACCEPTED SUCCESSFULLY!")
        print("LEVEL 2")
        print("RULE:\n1. At least 3 characters long.\n2. At least one lowercase letter.")
        code = input("Write a Password: ")
        if any(c.islower() for c in code) and len(code) >= 3:
            print("PASSWORD ACCEPTED SUCCESSFULLY!")
            print("LEVEL 3")
            print("RULE:\n1. At least 3 characters long.\n2. At least one lowercase letter.\n3. At least one uppercase letter.")
            code = input("Write a Password: ")
            if any(c.isupper() for c in code) >=1 and any(c.islower() for c in code) >=1 and len(code) >= 3:
                print("PASSWORD ACCEPTED SUCCESSFULLY!")
                print("LEVEL 4")
                print("RULE:\n1. At least 3 characters long.\n2. At least one digit (0-9).\n3. At least one symbol.")
                code = input("Write a Password: ")
                if any(c.isdigit() for c in code) >=1 and any(c in "!#$%&'()*+,-.:;<=>?@[]^_`{|}~" for c in code) >=1 and len(code) >= 3:
                    print("PASSWORD ACCEPTED SUCCESSFULLY!")
                    print("LEVEL 5")
                    print("RULE:\n1. At least 6 characters long.\n2. A mix of at least 3 character types(e.g., lowercase, uppercase, and digits).")
                    code = input("Write a Password: ")
                    if len(code) >= 6 and any(c.isupper()for c in code)>= 1 and any(c.islower() for c in code)>= 1 and any(c.isdigit() for c in code) >= 1:
                        print("PASSWORD ACCEPTED SUCCESSFULLY!")
                        print("LEVEL 6")
                        print("RULE:\n1. At least 8 characters long.\n2. At least two digits (0-9).\n3. At least two symbols.")
                        code = input("Write a Password: ")
                        if len(code) >= 8 and any(c.isdigit() for c in code) >=1 and any(c in "!#$%&'()*+,-.:;<=>?@[]^_`{|}~" for c in code) >= 1:
                            print("PASSWORD ACCEPTED SUCCESSFULLY!")
                            print("LEVEL 7")
                            print("RULE:\n1. At least 10 characters long.\n2. At least one character from all four character types (lowercase, uppercase, digit, and symbol).")
                            code = input("Write a Password: ")
                            if len(code) >= 10 and any(c.islower() and c.isupper() and c.isdigit() for c in code) >=1 or any(c in "!#$%&'()*+,-.:;<=>?@[]^_`{|}~" for c in code) >=1:
                                print("PASSWORD ACCEPTED SUCCESSFULLY!")
                                print("---YOU WON---")
                                quit()
                            else:
                                print("You Lose the Game!")
                                print("---GAME OVER---") 
                        else:
                            print("You Lose the Game!")
                            print("---GAME OVER---")
                    else:
                        print("You Lose the Game!")
                        print("---GAME OVER---")
                else:
                    print("You Lose the Game!")
                    print("---GAME OVER---")
            else: 
                print("You Lose the Game!")
                print("---GAME OVER---")
        else:
            print("You Lose the Game!")
            print("---GAME OVER---")
    else:
        print("You Lose the Game!")
        print("---GAME OVER---")
elif select == 3:
    quit()