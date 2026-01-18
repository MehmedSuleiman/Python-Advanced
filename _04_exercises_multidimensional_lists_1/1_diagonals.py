#Using a nested list comprehension, write a program that reads rows of a square matrix and its elements,
# separated by a comma and a space ", ".
# You should find the matrix's diagonals, print them, and their sum in the format:
#"Primary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_primary}
#Secondary diagonal: {element1}, {element2}, … {elementN}. Sum: {sum_of_secondary}".
from tokenize import endpats

rows_col = int(input())

matrix = [[int(x) for x in input().split(", ")] for _ in range(rows_col)]
diagonal_1 = [matrix[x][x] for x in range(rows_col)]
diagonal_1_sum = sum(diagonal_1)
print(f"Primary diagonal: {', '.join(str(i) for i in diagonal_1)}. Sum: {diagonal_1_sum}")
diagonal_2 = [matrix[x][rows_col-1-x] for x in range(rows_col)]
diagonal_2_sum = sum(diagonal_2)
print(f"Secondary diagonal: {', '.join(str(i) for i in diagonal_2)}. Sum: {diagonal_2_sum}")
