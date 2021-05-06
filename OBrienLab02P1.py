user_num = int(input("Please enter a number: "))
if user_num % 2 == 0:
    print("Even number!")
    if user_num < 0:
        print("Negative number!")
elif user_num % 2 != 0:
    print("Odd number!")
    if user_num < 0:
        print("Negative number!")
