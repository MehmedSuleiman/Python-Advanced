#Write a program that finds the difference between the sums of the square matrix diagonals(absolute value).
 #On the first line, you will receive an integer N - the size a square matrix.
#The following N lines hold the values for each column - N numbers separated by a single space.
#Print the absolute difference between the primary and the secondary diagonal sums.

rows_col = int(input())

matrix = [[int(x) for x in input().split(" ")] for _ in range(rows_col)]

diagonal_1 = [matrix[x][x] for x in range(rows_col)]
diagonal_1_sum = sum(diagonal_1)

diagonal_2 = [matrix[x][rows_col-1-x] for x in range(rows_col)]
diagonal_2_sum = sum(diagonal_2)

print(abs(diagonal_1_sum - diagonal_2_sum))