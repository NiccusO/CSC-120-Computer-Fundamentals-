# constants
# A = 3
# B = -2
# C = 7
# input statements

x = int(input("Please enter an integer: "))
y = int(input("Please enter another integer: "))
z = int(input("Please enter a third integer: "))

print("The numbers entered are: ", x, ", and", y, ", and ", z)
sum_user_num = x + y + z
max_user_num = max(x, y, z)
min_user_num = min(x, y, z)
product_user_num = x*y*z
avg_user_num = sum_user_num/3
sum_to_min = sum_user_num**min_user_num
sum_div_min = sum_user_num/min_user_num
sum_floordiv_max = sum_user_num//max_user_num
min_max_avg = (min_user_num + max_user_num)/2
print("Values are SUM = ", sum_user_num, ", PRODUCT = ", product_user_num,  ", MAXIMUM = ",  max_user_num, ", MINIMUM = ", min_user_num, ", and AVERAGE = %.2f" % avg_user_num)
print("Fancy values are: SUM^MINIMUM = ", sum_to_min, ", SUM divided by MINIMUM = ", sum_div_min, ", SUM divided by MAXIMUM with floor = ", sum_floordiv_max,
      ", AVERAGE of MINIMUM and MAXIMUM = ", min_max_avg)
print("Your integers in ascending order: ", min_user_num, ", ", sum_user_num - (max_user_num + min_user_num), ", ", max_user_num)
# this is a comment
# the following if...else structure is used to illustrate the syntax
# note the3 indentation
# if (x > 0) :
#    x = A*x
#    x = B*x
# else:
#    y = C*y
#    y = A*y
# print("NEW value of x = ", x, " and ", " y ", y)
print()
print("My name is: Nicole O'Brien")
print("My major is Office Administration, but I'm really veering towards these programming courses!")
print("I am taking CSC-120 toward my Programming Fundamentals Certificate, and also to solidify some of what I've been learning in CSC-121 and CTI-110!")
print("Five years from now, I hope to have a successful career using some of what I've learned in this course!")
