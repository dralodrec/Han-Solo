def F_exitCondi(prompt, count):
    while True:
        user_input = input(prompt)
        if (user_input != "END"):
            try:
                user_input = int(user_input)
            except:
                print(f"Entry must be greater than zero or an integer")
            else:
                if (user_input == 0):
                    print(f"Incorrect Entry")
                elif (len(str(user_input)) < count or len(str(user_input)) > count ):
                    print(f"Please enter correct format")
                else:
                    print(user_input)
        else:
            print("\nGood Bye!\n\n")

F_exitCondi("enter: ", 10)          