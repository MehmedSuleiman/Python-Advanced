#Write a program that reads a rectangular matrix's dimensions and finds the 3x3 square with a maximum sum of
# its elements. There will be no case with two or more 3x3 squares with equal maximal sum.
#Input
#•	On the first line, you will receive the rows and columns in the format "{rows} {columns}" – integers in the range [1, 20]
#•	On the following lines, you will receive each row with its columns - integers,
# separated by a single space in the range [-20, 20]
#Output
#•	On the first line, print the maximum sum of the elements in the 3x3 square in the format "Sum = {sum}"
#•	On the following 3 lines, print each element of the found submatrix, separated by a single space

rows, cols = [int(i) for i in input().split()]

matrix = [[int(i) for i in input().split()] for _ in range(rows)]

max_sum = float('-inf')
max_matrix = None


for i in range(rows-2):
    for j in range(cols- 2):
        ls = None
        first = matrix[i][j]
        second = matrix[i][j+1]
        third = matrix[i][j+2]
        fourth = matrix[i+1][j]
        fifth = matrix[i+1][j+1]
        sixth = matrix[i+1][j+2]
        seventh = matrix[i+2][j]
        eighth = matrix[i+2][j+1]
        ninth = matrix[i+2][j+2]
        ls = [first, second, third, fourth, fifth, sixth, seventh, eighth, ninth]
        if sum(ls) > max_sum:
            max_sum = sum(ls)
            max_matrix = [[first, second, third], [fourth, fifth, sixth], [seventh, eighth, ninth]]
        else:
            pass

print(f"Sum = {max_sum}")
for row in max_matrix:
    print(*row, sep=" ")



