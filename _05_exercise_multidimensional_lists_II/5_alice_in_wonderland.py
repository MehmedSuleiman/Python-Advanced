#Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
#You will be given an integer n for the size of the Wonderland territory with a square shape.
# On the following n lines, you will receive the rows of the territory:
#•	Alice will be placed in a random position, marked with the letter "A".
#•	On the territory, there will be bags of tea, represented as numbers.
# If Alice steps on a number position, she collects the tea bags and increases the quantity with the corresponding number.
#•	There will always be one rabbit hole on the territory marked with the letter "R".
#•	All of the empty positions will be marked with ".".
#After the field state, you will be given commands for Alice's movements.
# Move commands can be: "up", "down", "left" or "right".
##In the end, the path she walked had to be marked with '*'.
#For more clarifications, see the examples below.
##•	On the first line, you will be given the integer n – the size of the square matrix
#•	On the following n lines - matrix representing the field (each position separated by a single space)
#•	On each of the following lines, you will be given a move command
#Output
#•	On the first line:
#o	If Alice steps into the rabbit hole or goes out of the territory, print:
#"Alice didn't make it to the tea party."
#o	If she collected at least 10 bags of tea, print:
#"She did it! She went to the party."
#•	On the following lines, print the matrix.
##•	Alice will always either go outside Wonderland or collect 10 bags of tea
#•	All the commands will be valid
#•	All of the given numbers will be valid integers in the range [0, 10]

n = int(input())

matrix = []
alice = None

for i in range(n):
    part = input().split()
    matrix.append(part)
    for j in range(n):
        if part[j] == "A":
            alice = [i, j]

moves = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1)
}
alice_party = False
tea_packs = 0

while True:
    move = input()
    n_row = None
    n_col = None
    if move in moves:
        row, col = moves[move]
        n_row = alice[0] + row
        n_col = alice[1] + col
        if 0 > n_row or n_row >= n or 0 > n_col or n_col >= n:
            matrix[alice[0]][alice[1]] = "*"
            break
        matrix[alice[0]][alice[1]] = "*"
        alice= [n_row, n_col]

    if matrix[n_row][n_col].isdigit():
        tea_packs += int(matrix[n_row][n_col])
    elif matrix[n_row][n_col] == "R":
        matrix[alice[0]][alice[1]] = "*"
        break
    if tea_packs >= 10 :
        matrix[alice[0]][alice[1]] = "*"
        alice_party = True
        break

if alice_party:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]