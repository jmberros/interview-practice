# BST Sequences: A binary search tree was created by traversing through an array
# from left to right and inserting each element. Given a binary search tree with
# distinct elements, print all possible arrays that could have led to this tree.

# EXAMPLE Input:
#    2
#  1   3
# Output: {2, 1, 3}, {2, 3, 1}

from binarytree import Node, bst


def bst_sequences(root: Node) -> list[list[int]]:
    pass

#
#
#
# Test cases:
#


r = bst(3)
print(r)
result = bst_sequences(r)
for array in result:
    print(array)
