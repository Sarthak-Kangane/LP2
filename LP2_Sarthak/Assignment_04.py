# Solve the n-Queens problem using backtracking and branch-and-bound

def solve_n_queens(n):
    """
    Returns one solution for the n-Queens problem as a list of column indices,
    where the index in the list is the row number.
    """
    def is_safe(positions, row, col):
        # Check against all previously placed queens
        for r in range(row):
            c = positions[r]
            # Same column
            if c == col:
                return False
            # Same diagonal
            if abs(row - r) == abs(col - c):
                return False
        return True

    def place_queen(positions, row):
        # If all queens are placed, return True to stop recursion
        if row == n:
            return True
        # Try placing queen in each column
        for col in range(n):
            if is_safe(positions, row, col):
                positions[row] = col
                # Recurse to place next queen
                if place_queen(positions, row + 1):
                    return True
        # No valid position found in this row, backtrack
        return False

    # Initialize positions with -1 (no queen placed)
    positions = [-1] * n
    if place_queen(positions, 0):
        return positions
    else:
        return None

if __name__ == "__main__":
    n = 4
    solution = solve_n_queens(n)
    if solution:
        print(f"One solution for {n}-Queens: {solution}")
    else:
        print("No solution exists.")