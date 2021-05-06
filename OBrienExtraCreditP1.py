user_num = input("Please enter a digit: ")
user_numb = user_num.strip("-")
user_numb = user_numb.replace(".", "")
while user_numb.isdigit():
    print("You entered: ", user_num)
    user_num = input("Please enter a digit: ")
    user_numb = user_num.strip("-.")
    user_numb = user_numb.replace(".", "")
else:
    print("You did not enter a digit. Terminating program.")
# had a tricky time getting this to read negative or float numbers!
# It wouldn't allow me to strip . from floats, so used replace.
# I did a second attempt with a function:
# def check_if_digit(user_num):
#     user_numb = user_num.strip("-")
#     user_numb = user_numb.replace(".","")
#     return user_numb
#
# def main():
#     user_num = input("Please enter a digit: ")
#     user_numb = check_if_digit(user_num)
#     while user_numb.isdigit():
#         print("You entered: ", user_num)
#         user_num = input("Please enter a digit: ")
#         user_numb = check_if_digit(user_num)
#     else:
#         print("You did not enter a digit. Terminating program.")
#
# main()
