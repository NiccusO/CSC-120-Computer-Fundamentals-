even_to_20 = []
first_20_even = []
for i in range(0, 40):
    if i % 2 == 0:
        first_20_even.append(i)
print("The first 20 even numbers: ", first_20_even)

for i in range(0, 21):
    if i % 2 == 0:
        even_to_20.append(i)
print("The first even numbers from 0 to 20:", even_to_20)

# wasn't sure if you wanted a *total of 20* of the first even numbers or the
# first even numbers *up to* 20...
# I did them both, but in a list to make it easier to read.)
