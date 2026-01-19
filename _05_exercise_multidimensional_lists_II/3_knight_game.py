#Chess is the oldest game, but it is still popular these days.
# You will use only one chess piece for this task - the Knight.
#A chess knight has 8 possible moves it can make, as illustrated.
# It can move to the nearest square but not on the same row, column, or
# diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one square
# horizontally then two squares vertically - i.e., in an "L" pattern.)
#The knight game is played on a board with dimensions N x N.
#You will receive a board with a "K" for knights and a "0" for empty cells.
# Your task is to remove knights until no knights that can attack one another with one move are left.
#Always remove the knight who can attack the greatest number of knights.
# If there are two or more knights with the same number of attacks, remove the top-left one.
#Input
#•	On the first line, you will receive integer N - the size of the board
#•	On the following N lines, you will receive strings with "K" and "0"
#Output
#•	Print a single integer with the number of knights that need to be removed.
#Constraints
#•	The size of the board will be 0 < N < 30
#•	Time limit: 0.3 sec. Memory limit: 16 MB

def count_attacks(board, r, c, n):
    moves = [
        (-2, -1), (-2, 1),
        (-1, -2), (-1, 2),
        (1, -2),  (1, 2),
        (2, -1),  (2, 1)
    ]
    attacks = 0
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == "K":
            attacks += 1
    return attacks

n = int(input())
board = [list(input()) for _ in range(n)]

removed_knights = 0

while True:
    max_attacks = 0
    knight_pos = None

    for r in range(n):
        for c in range(n):
            if board[r][c] == "K":
                attacks = count_attacks(board, r, c, n)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_pos = (r, c)

    if max_attacks == 0:
        break

    r, c = knight_pos
    board[r][c] = "0"
    removed_knights += 1

print(removed_knights)
