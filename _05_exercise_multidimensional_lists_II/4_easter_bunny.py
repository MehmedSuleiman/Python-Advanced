#Your task is to collect as many eggs as possible.
#On the first line, you will be given a number representing the size of the field.
# In the following few lines, you will be given a field with:
#•	One bunny - randomly placed in it and marked with the symbol "B"
#•	Number of eggs placed at different positions of the field and traps marked with "X"
#Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs.
# The directions that should be considered as possible are up, down, left, and right.
# If you reach a trap while checking some of the directions, you should not consider the
# fields after the trap in this direction. The bunny can move within the field and cannot go outside its boundaries.
# Do not consider negative indices as valid ones. For more clarifications, see the examples below.
#Note: In some directions, the collected eggs can happen to be zero or a negative number.
#Input
#•	A number representing the size of the field
#•	The matrix representing the field (each position separated by a single space)
#Output
#•	The direction which should be considered as best (lowercase)
##•	The total number of eggs collected
#Constraints
#•	There will NOT be two or more paths consisting of the same total amount of eggs.

n = int(input())

matrix = []
bunny = None


for i in range(n):
    matrix.append(list(input().split()))
    for j in range(n):
        if matrix[i][j] == 'B':
            bunny = (i, j)


directions ={
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

best_direction = None
best_eggs = float('-inf')
best_path = []

for name, (dr, dc) in directions.items():
    r, c = bunny
    path = []
    eggs = 0
    r += dr
    c += dc
    while 0 <= r < n and 0 <= c < n:
        cell = matrix[r][c]
        if cell == 'X':
            break
        eggs += int(cell)
        path.append([r, c])
        r += dr
        c += dc
    if eggs > best_eggs:
        best_eggs = eggs
        best_direction = name
        best_path = path


print(best_direction)
for p in best_path:
    print(p)
print(best_eggs)

