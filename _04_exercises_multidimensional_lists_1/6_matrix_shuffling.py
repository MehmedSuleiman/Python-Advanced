#Write a program that reads a matrix from the console and performs certain operations with its elements.
# User input is provided similarly to the problems above - first, you read the dimensions and then the data.
#Your program should receive commands in the format:
# "swap {row1} {col1} {row2} {col2}" where ("row1", "col1") and ("row2", "col2") are the coordinates of two
# points in the matrix. A valid command starts with the "swap" keyword along with four valid coordinates
# (no more, no less), separated by a single space.
#•	If the command is valid, you should swap the values at the given indexes and print the matrix at each step
# (thus, you will be able to check if the operation was performed correctly).
#•	If the command is not valid (does not contain the keyword "swap", has fewer or more coordinates entered,
# or the given coordinates are not valid), print "Invalid input!" and move on to the following command.
# A negative value makes the coordinates not valid.
#Your program should finish when the command "END" is entered.

def is_valid(row, col, row2, col2, n_rol, n_col):
    return 0 <=row and row <= n_rol and 0<=col  and col <= n_col and 0<=row2 and row2 <=n_rol and 0<=col2 and col2<=n_col

row, col = map(int, input().split())

matrix = [input().split() for _ in range(row)]

while True:
    com = input()
    if com == "END":
        break
    else:
        command = com.split()
        if command[0] == "swap" and len(command) == 5:
            row1, col1, row2, col2 = [int(i) for i in command[1:]]
            valid = is_valid(row1, col1, row2, col2, row, col)
            if valid:
                matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
                for r in matrix:
                    print(*r)
            else:
                print("Invalid input!")
        else:
            print("Invalid input!")


