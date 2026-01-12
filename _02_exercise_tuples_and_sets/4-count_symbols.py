#Write a program that reads a text from the console and counts the occurrences of each character in it.
# Print the results in alphabetical (lexicographical) order.

text = tuple(sorted(input()))

sumbols = {}

for char in text:
    if char in sumbols:
        sumbols[char] += 1
    else:
        sumbols[char] = 1

for key, value in sumbols.items():
    print(f"{key}: {value} time/s")

