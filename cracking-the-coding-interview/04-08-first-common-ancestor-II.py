# First Common Ancestor: Design an algorithm and write code to find the first
# common ancestor of two nodes in a binary tree. Avoid storing additional nodes
# in a data structure. NOTE: This is not necessarily a binary search tree.


# 1. With links to parents
# 2. Without links to parents

# Assuming the nodes DO NOT have a link to their parent.
# 💡
# Es medio rara la solución, porque el constraint es grande.
# La idea es comenzar en el root y mirar si el nodo 1 está a izquierda o a derecha.
# Lo mismo para el nodo 2.
# Si están del mismo lado, repetimos yendo hacia ese lado (e.g. root = root.left
# si están los dos a la izquierda). Si están en distinto lado, el root es el FCA!
# Hay que manejar los corner cases por separado:
# Si son el mismo nodo o si uno de ellos es el root (o sea uon de ellos en el
# FCA del otro!).


from binarytree import Node


def get_depth(node: Node) -> int:
    depth = 1
    while node and node.parent:
        node = node.parent
        depth += 1
    return depth


def covers(root: Node, node: Node) -> bool:
    if not root:
        return False
    if root is node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def first_common_ancestor(root, node1, node2):
    if node1 == node2:
        return node1
    if root == node1:
        return node1
    if root == node2:
        return node2

    print(f"{root.value = }")
    covers1_left = covers(root.left, node1)
    covers1_right = covers(root.right, node1)

    covers2_left = covers(root.left, node2)
    covers2_right = covers(root.right, node2)

    assert covers1_left or covers1_right
    assert covers2_left or covers2_right

    # The nodes are on the same side
    if covers1_left and covers2_left:
        return first_common_ancestor(root.left, node1, node2)
    if covers1_right and covers2_right:
        return first_common_ancestor(root.right, node1, node2)

    # The nodes are on different sides, this is the common ancestor
    return root.value


#
# Test case
#

nodes = {i: Node(i) for i in range(1, 15)}

nodes[7].parent = nodes[5]
nodes[5].parent = nodes[2]
nodes[4].parent = nodes[2]
nodes[2].parent = nodes[1]
nodes[3].parent = nodes[1]
nodes[6].parent = nodes[3]
nodes[1].parent = None
nodes[8].parent = nodes[4]

nodes[1].left = nodes[2]
nodes[1].right = nodes[3]
nodes[2].left = nodes[4]
nodes[2].right = nodes[5]
nodes[5].left = nodes[7]
nodes[3].left = nodes[6]
nodes[4].right = nodes[8]

r = nodes[1]
node_extra = Node(-1)
node_extra.parent = None

print(r)
result = first_common_ancestor(r, nodes[8], nodes[3])  # => Node(2)
print(f"{result = }")






# This DOES store values in an additional data structure, so it does not count
# as a solution ;___;
# def first_common_ancestor(root: Node, node1: Node, node2: Node) -> Node | None:
#     print(f"{root = }, {node1 = }, {node2 = }")

#     node1_path = []
#     node2_path = []
#     current_path = []

#     def dfs(node):
#         nonlocal node1_path, node2_path, current_path

#         if node1_path and node2_path:
#             return  # Both nodes have been found, bubble up!

#         current_path.append(node.value)
#         print(f"Visiting {node.value} -- {current_path}")

#         if node is node1:
#             node1_path = list(current_path)
#             print("  Found node 1!")
#         if node is node2:
#             node2_path = list(current_path)
#             print("  Found node 2!")

#         if node.left:
#             dfs(node.left)
#         if node.right:
#             dfs(node.right)

#         current_path.pop()

#     dfs(root)

#     if not node1_path or not node2_path:
#         return None  # They are in different trees

#     n = min([len(node1_path), len(node2_path)])

#     common_ancestor = None
#     for i in range(n):
#         if node1_path[i] == node2_path[i]:
#             common_ancestor = node1_path[i]
#         else:
#             break

#     return common_ancestor
