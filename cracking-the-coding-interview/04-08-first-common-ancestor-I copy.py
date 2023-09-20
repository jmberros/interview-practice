# First Common Ancestor: Design an algorithm and write code to find the first
# common ancestor of two nodes in a binary tree. Avoid storing additional nodes
# in a data structure. NOTE: This is not necessarily a binary search tree.


# 1. With links to parents
# 2. Without links to parents


# 1. Assuming each node has a link to its parent.
# 💡
# El truco acá es "alinear" ambos punteros en el mismo nivel yendo hacia arriba.
# Para esto necesito la profundidad de ambos, lo que implica ir hacia arriba
# hasta el root para cada uno.
# Luego ir subiendo a la par hasta que coincida el nodo (si nunca coinciden,
# no están en el mismo árbol!).

from binarytree import Node


def get_depth(node: Node) -> int:
    depth = 1
    while node and node.parent:
        node = node.parent
        depth += 1
    return depth


def first_common_ancestor(node1: Node, node2: Node) -> Node | None:
    print(f"{node1 = }, {node2 = }")
    depth1 = get_depth(node1)
    depth2 = get_depth(node2)
    print(f"{depth1 = }, {depth2 = }")

    depth_diff = abs(depth1 - depth2)
    for _ in range(depth_diff):
        if depth1 > depth2:
            node1 = node1.parent
        else:
            node2 = node2.parent

    # At this point both pointers are in the same depth/level
    while node1 and node2:
        if node1 is node2:
            return node1  # This is the FCA!

        node1 = node1.parent
        node2 = node2.parent

    return None


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

root = nodes[1]
node_extra = Node(-1)
node_extra.parent = None

print(root)

result = first_common_ancestor(nodes[8], node_extra)  # => Node(2)
print(f"{result = }")
