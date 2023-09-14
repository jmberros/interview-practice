# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
# its entire row and column are set to 0.

# 💡
# visitás todas las celdas y guardás rows y cols para borrar.
# Luego visitás de nuevo esas rows y borrás cada celda, y lo mismo las cols.
# Hacés 3 veces N x M, o sea O(N x M).

test_cases = [
    (
        [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    (
        [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
        [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
]


# Time: O(N x M)
# Space: O(N + M)
def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """Zeroes out cols and rows that contain any zeroes. IN PLACE."""
    rows_to_zero = set()
    cols_to_zero = set()

    m = len(matrix)
    n = len(matrix[0])

    for row in range(m):
        for col in range(n):
            if matrix[row][col] == 0:
                rows_to_zero.add(row)
                cols_to_zero.add(col)

    for row in rows_to_zero:
        for col in range(n):
            matrix[row][col] = 0

    for col in cols_to_zero:
        for row in range(m):
            matrix[row][col] = 0

    return matrix


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, zero_matrix)
