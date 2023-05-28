total_solutions = 0


def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    backtrack(board, 0, n)
    print("Total solutions:", total_solutions)


def backtrack(board, col, n):
    global total_solutions
    if col == n:
        # All queens are placed, found a solution
        total_solutions += 1
        print_board(board)
        return

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            backtrack(board, col + 1, n)
            board[row][col] = 0  # Remove the queen (backtrack)


def is_safe(board, row, col, n):
    # Check if the current position is safe for a queen

    # Check the left side of the current row
    for c in range(col):
        if board[row][c] == 1:
            return False

    # Check the upper diagonal on the left side
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1

    # Check the lower diagonal on the left side
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
    return True


def print_board(board):
    n = len(board)
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                print("Q ", end="")
            else:
                print(". ", end="")
        print()
    print()


if __name__ == '__main__':
    num_queens = int(input("Enter the number of queens: "))
    solve_n_queens(num_queens)
