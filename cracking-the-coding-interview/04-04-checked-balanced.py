# Check Balanced: Implement a function to check if a binary tree is balanced.
# For the purposes of this question, a balanced tree is defined to be a tree
# such that the heights of the two subtrees of any node never differ by more
# than one.

# 💡
# Acá es evidente que se necesita recursividad, pero el truco está en darse
# cuenta de que hay que ir chequeando la profundidad a izquierda y a derecha
# recursivamente, hasta las hojas (donde depth = 0 y balanced = True).
# También hay que ir chequeando a derecha y a izquierda si los subtrees están
# balanceados. Luego es un álgebra mínima para ver si el current node está
# balanceado.
#
# La función recursiva NO es la misma que la de la solución, porque la recursiva
# necesita retornar dos cosas (depth y is_balanced), mientras que la de la solución
# sólo el is_balanced final, del root node. Así que implementarla como helper
# y llamarla una sola vez.


from binarytree import tree, Node


def get_depth_and_balanced_status(node: Node) -> tuple[int, bool]:
    if node.left:
        depth_left, balanced_left = get_depth_and_balanced_status(node.left)
    else:
        depth_left, balanced_left = 0, True
    if node.right:
        depth_right, balanced_right = get_depth_and_balanced_status(node.right)
    else:
        depth_right, balanced_right = 0, True

    is_balanced = (
        abs(depth_left - depth_right) <= 1 and balanced_left and balanced_right
    )
    depth = max(depth_left, depth_right) + 1
    print(f"{node.value = }, {depth_left = }, {depth_right = }, {is_balanced = }, {depth = }")
    return depth, is_balanced


def check_balanced(root: Node) -> bool:
    _, is_balanced = get_depth_and_balanced_status(root)
    return is_balanced


balanced_root = tree(3)
print(balanced_root)
print(get_depth_and_balanced_status(balanced_root))

unbalanced_root = Node(1)
unbalanced_root.right = Node(2)
unbalanced_root.right.right = Node(3)
unbalanced_root.right.right.right = Node(4)
print(unbalanced_root)
print(get_depth_and_balanced_status(unbalanced_root))
