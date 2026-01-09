#Write a program that reads a string with N integers from the console, separated
# by a single space, and reverses them using a stack.
# Print the reversed integers on one line, separated by a single space.

n = input().split()
stack = []

for num in range(len(n)):
    stack.append(n.pop())

print(' '.join(stack))

      # second solution
# for num in range(len(n)):
#     number = n.pop()
#     print(number, end = ' ')