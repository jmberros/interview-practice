# Validate BST: Implement a function to check if a binary tree is a binary
# search tree.

# 💡
# Recursión actualizando un rango de valores permitidos.
# Cada vez que bajás a izquierda, actualizás el máximo con el nodo corriente.
# Cada vez que bajás a derecha, actualizás el mínimo con el nodo corriente.
# En cada call, comparás el valor del current node con ese rango.

from binarytree import Node


class InvalidBstException(Exception):
    pass


def validate_bst(
    node: Node,
    range_: tuple[int, int] = (float("-inf"), float("+inf"))
) -> bool:

    if node.value < range_[0] or node.value > range_[1]:
        print(f"Node {node.value} is invalid | {range_ = }")
        return False

    left_valid = validate_bst(node.left, (range_[0], node.value)) if node.left else True
    right_valid = validate_bst(node.right, (node.value, range_[1])) if node.right else True

    return left_valid and right_valid


root_bst = Node(3)
root_bst.left = Node(2)
root_bst.right = Node(5)
root_bst.left.left = Node(0)
root_bst.right.left = Node(4)
root_bst.right.right = Node(8)
print(root_bst, validate_bst(root_bst))
print("---")

root_bt = Node(2)
root_bt.left = Node(1)
root_bt.right = Node(3)
root_bt.left.right = Node(10)
root_bt.right.left = Node(1)
print(root_bt, validate_bst(root_bt))
