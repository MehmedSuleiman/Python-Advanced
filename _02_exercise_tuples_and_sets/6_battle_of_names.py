#You will receive a number N. On the following N lines, you will be receiving names.
# You should sum the ASCII values of each letter in the name and integer divide it by the
# number of the current row (starting from 1).
# Save the result to a set of either odd or even numbers, depending on whether the resulting number is odd or even.
# After that, sum the values of each set.
#•	If the sums of the two sets are equal, print the union of the values, separated by ", ".
#•	If the sum of the odd numbers is bigger than the sum of the even numbers, print the different values, separated by ", ".
#•	If the sum of the even numbers is bigger than the sum of the odd numbers,
#   print the symmetric-different values, separated by ", ".
#NOTE: On every operation, the starting set should be the odd set

set_of_odd = set()
set_of_even = set()

for name in range(1, int(input()) + 1):
    current_name = input()
    value_of_name = sum(ord(char) for char in current_name) // name
    if value_of_name % 2 == 0:
        set_of_even.add(value_of_name)
    else:
        set_of_odd.add(value_of_name)


if sum(set_of_even) == sum(set_of_odd):
    print(*(set_of_odd | set_of_even), sep=", ")
elif sum(set_of_odd) > sum(set_of_even):
    print(*(set_of_odd - set_of_even), sep=", ")
else:
    print(*(set_of_odd ^ set_of_even), sep=", ")

