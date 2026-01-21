#Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.
# The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.
# Submit only the function in the judge system.

def even_odd(*args):
    command = args[-1]
    numbers = args[:-1]

    if command == "even":
        return [n for n in numbers if n % 2 == 0]
    else:
        return [n for n in numbers if n % 2 != 0]

