#Write a program to generate the following matrix of palindromes of 3 letters with r rows and c columns
# like the one in the examples below.
#•	Rows define the first and the last letter: row 0  'a', row 1  'b', row 2  'c', …
#•	Columns + rows define the middle letter:
#o	column 0, row 0  'a', column 1, row 0  'b', column 2, row 0  'c', …
#o	column 0, row 1  'b', column 1, row 1  'c', column 2, row 1  'd', …
##•	The numbers r and c stay at the first line at the input in the format "{rows} {columns}"
#•	r and c are integers in the range [1, 26]

rows, cols = [int(i) for i in input().split()]

matrix = []
letter = "a"

for r in range(rows):
    for c in range(cols):
        first_letter = ""
        second_letter = ""
        third_letter = ""

        if r != 0:
            first_letter, third_letter = chr(ord("a") + r), chr(ord("a") + r)
        else:
            first_letter, third_letter = "a", "a"

        if c != 0:
            second_letter = chr(ord("a")+ c +r)
        else:
            second_letter = chr(ord("a") + r)
        matrix.append([first_letter, second_letter, third_letter])

for r in range(len(matrix)):
    if r% cols == 0:
        print(end= "\n")
    else:
        print(*matrix[r], sep="", end=" ")




