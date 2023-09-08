# https://leetcode.com/problems/rotate-image/description/
# Rotate Matrix: Given an image represented by an NxN matrix, where each pixel
# in the image is 4 bytes, write a method to rotate the image by 90 degrees. Can
# you do this in place?
import math

test_cases = [
    (
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    (
        [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
        [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]],
    ),
]

# (1) Reverse the matrix rows
#
# 7 8 9
# 4 5 6
# 1 2 3
#
# (2) Transpose: rows <-> cols
#
# 7 4 1
# 8 5 2
# 9 6 3

# Time: O(N^2)
# Space: O(1)
def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Rotates an NxN matrix IN PLACE."""
    n = len(matrix)

    # (1) Reverse the matrix rows
    # This can be done with: matrix.reverse()
    i, j = 0, n - 1
    while i < j:
        matrix[i], matrix[j] = matrix[j], matrix[i]
        i += 1
        j -= 1

    # (2) Transpose the matrix, swap all (i < j) pairs
    for i in range(n):
        for j in range(n):
            if i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


if __name__ == "__main__":
    from helpers import run_test_cases

    run_test_cases(test_cases, rotate)
