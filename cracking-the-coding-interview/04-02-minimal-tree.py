# Minimal Tree: Given a sorted (increasing order) array with unique integer
# elements, write an algorithm to create a binary search tree with minimal
# height.

# 💡
# El truco es encontrar el valor del medio --como está ordenado, es el
# índice n // 2. Ese el es el root, luego para la mitad izquierda llamamos
# a la misma función recursivamente, y es el left subtree. Lo mismo para la
# mitad derecha, recursivamente. hasta que no hay mitades alrededor del
# middle value, entonces es una hoja.

from binarytree import Node


def minimal_tree(a: list[int]) -> Node:
    n = len(a)
    i = n // 2
    print(f"{a = }, {n = }, {i = }")
    middle_value = a[i]
    middle_node = Node(middle_value)
    left_half = a[:i]
    right_half = a[i + 1:]
    middle_node.left = minimal_tree(left_half) if left_half else None
    middle_node.right = minimal_tree(right_half) if right_half else None
    return middle_node


a = [1, 3, 5, 6, 7, 10, 20]
mt = minimal_tree(a)
print(mt)
