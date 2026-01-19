#Write a program that reads a matrix from the console and changes its values.
# On the first line, you will get the matrix's rows - N.
# You will get elements for each column on the following N lines, separated with a single space.
# You will be receiving commands in the following format:
#•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
#•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
#If the coordinate is invalid, you should print "Invalid coordinates".
# A coordinate is valid if both of the given indexes are in the range [0; len() – 1].
#When you receive "END", you should print the matrix and stop the program.
def is_valid(matrix, row, column):
    return 0 <= column < len(matrix[0]) and 0 <= row  < len(matrix)


n = int(input())

matrix = [[int(i) for i in input().split()] for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break

    com, row, col, num = command.split()
    if is_valid(matrix, int(row), int(col)):
        if com == "Add":
            matrix[int(row)][int(col)] += int(num)
        else:
            matrix[int(row)][int(col)] -= int(num)
    else:
        print("Invalid coordinates")

[print(*row, sep= " ") for row in matrix]
