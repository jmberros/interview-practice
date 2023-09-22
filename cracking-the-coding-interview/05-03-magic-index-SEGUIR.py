# Magic Index: A magic index in an array A[0...n-1] is defined to be an index
# such that A[i] = i. Given a sorted array of distinct integers, write a method
# to find a magic index, if one exists, in array A.

# FOLLOW UP: What if the values are not distinct?

#
#   0  1 2 3 4 5 6
# [-2 -1 0 2 4 7 9 ]  magic index = 4

# If at any point, A[i] > i, then no magic index can be found ahead

#   0  1 2 3 4 5 6
# [-2 -1 0 2 4 7 9 ]  mid index = 3, mid value = 2,  A[i] < i, go right

#            4 5 6
#          [ 4 7 9 ]  mid index = 5, A[5] = 7 > 5, go left

#           4
#          [4]  mid index = 4, A[4] = 4, this is it!

# --------
#  0 1 2
# [1 2 3] mid index = 1, A[1] = 2 > 1, go left A[:1]

#  0
# [1] mid index = 0, A[0] = 1 > 0, can't go left anymore, no magic index!


def magic_index_brute(array):
    for i, value in enumerate(array):
        if i == value:
            return i
    return -1


def magic_index_while(array: list[int]) -> int:
    a, b = 0, len(array) - 1

    while a <= b:
        mid = (a + b) // 2
        if array[mid] == mid:
            return mid
        if array[mid] > mid:  # Go left
            b = mid - 1
        else:  # Go right
            a = mid + 1

    return -1


def magic_index_helper(array: list[int], start: int, end: int) -> int:
    if start > end:
        return -1

    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    if array[mid] > mid:  # Go left
        return magic_index_helper(array, start, mid - 1)
    else:  # Go right
        return magic_index_helper(array, mid + 1, end)


def magic_index(array: list[int]) -> int:
    return magic_index_helper(array, 0, len(array) - 1)


arr = [-2, -1, 0, 2, 4, 7, 9]
print(arr, magic_index(arr), " should be 4")

arr = [0, 1, 2]
print(arr, magic_index(arr), " should be None")
