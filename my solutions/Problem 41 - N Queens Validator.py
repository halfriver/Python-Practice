# Problem 41: N Queens
 # given n, find all the possible positions of n queens positioned on an n by n board such that they do not impede each others' possible movements
 
# Original: 11 December 2019
# Edited: 08 December 2020

solutions = []
board_null = []

# print the board
def show_board(board):
    for row in range(len(board)):
        print(board[row])

# can a Queen be placed at this spot
def safe(board, row_index, column_index, n):
    print("safety test")
    if row_index == 0:
        print("row 0")
        return True
    # row
    if column_index > 0:
        for column in range(column_index):
            if board[row_index][column] != "-":
                print("safety fail row")
                return False
    # column
    for row in range(row_index):
        if board[row][column_index] != "-":
            print("safety fail column: for row " + str(row_index) + ", column " + str(column_index) + " because of " + str(row))
            return False
    # diagonal left
    if column_index != 0:
        for x in range(min([row_index, column_index])):
            if board[row_index-1][column_index-1] != "-":
                print("safety fail diag left")
                return False
    # diagonal right
    if column_index != n-1:
        for x in range(row_index - column_index):
            if board[row_index-1][column_index+1] != "-":
                print("safety fail diag right")
                return False
    print("safety pass")
    return True

# recursive; base case: completed board of safe Queens
def solve(board, row_index, column_index, n, solutions):
    show_board(board)
    if row_index == n-1:
        print(board)
        solutions.append(board)
        return True
    return_value = False
    for column in range(n):
        if safe(board, row_index, column, n):
            board[row_index][column] = "Q"
            return_value = solve(board, row_index+1, column, n, solutions) or return_value
            board[row_index][column] = "-"
    return return_value

# the input must be an integer
while True:
    n = input("Provide a value for n.\n")
    try:
        int(n)
    except:
        print("The value must be a number. Please try again.")
    else:
        n = int(n)
        break

# generate the virtual array
for x in range(n):
    board_null.append([])
    for y in range(n):
        board_null[x].append("-")

board = board_null
count = 0

# populate the board with n Queens, one per row
'''for a in range(n):
    count += 1
    print("initial for-loop: count " + str(count))
    board = board_null
    board[0][a] = "Q"
    solve(board, 1, 0, n, solutions)
'''
solve(board, 0, 0, n, solutions)

print("For n=" + str(n) + " Queens, there are " + str(len(solutions)) + " solutions.")
for solution in solutions:
    show_board(board)

