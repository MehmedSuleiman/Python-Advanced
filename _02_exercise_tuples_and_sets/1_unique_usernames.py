#Write a program that reads a sequence of N usernames from the console and maintains a
#collection of only the unique ones.
#On the first line, you will receive an integer N.
#On the following N lines, you will receive the usernames.
#Print the collection on the console (the order does not matter):

n = int(input())

usernames = set()

for username in range(n):
    usernames.add(input())


for username in usernames:
    print(username)