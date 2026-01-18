#Find the number of all 2x2 squares containing identical chars in a matrix.
# On the first line, you will receive the matrix's dimensions in the format "{rows} {columns}".
# In the following rows, you will receive characters separated by a single space.
# Print the number of all square matrices you have found.

rows, cols = [int(i) for i in input().split()]

matrix = [[i for i in input().split()] for _ in range(rows)]

x = 0

for i in range(rows-1):
    for j in range(cols- 1):
        first = matrix[i][j]
        second = matrix[i][j+1]
        third = matrix[i+1][j]
        fourth = matrix[i+1][j+1]
        if first == second and first == third and first == fourth:
            x += 1
        else:
            pass

print(x)