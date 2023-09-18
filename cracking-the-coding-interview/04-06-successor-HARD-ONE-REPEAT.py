# Successor: Write an algorithm to find the "next" node (i.e., in-order
# successor) of a given node in a binary search tree. You may assume that each
# node has a link to its parent.


# NOTE: in-order traversal is 1. left child, 2. node, 3. right child
# 💡
# Si estamos haciendo in-order, el próximo nodo es está a la DERECHA!
# Dividir por casos:
# Si hay right subree, bajás al a derecha y querés el LEFTMOST node del right subtree.
# Si no, subís hasta que hayas subido desde la izquierda, o sea parent.left == child
# Esto cabe en while loop muy conciso pero al que hay que llegar pensando,
# no sale tan de una. Mirarlo.
# Podría no haber successor, si estás en el rightmost node del árbol, atenti.

from binarytree import Node


# If this node has a right subtree:
# return the LEFTMOST node of the right subtree
# If not:
# we are done traversing everything under this node
# we need to go up
# -- If this node is the LEFT child of its parent => return PARENT
# -- If this node is the RIGHT child of its parent => go up and repeat
#

def successor(node: Node) -> int | None:
    if node.right:
        current = node.right
        while current.left:
            current = current.left
        return current.value

    ancestor = node.parent
    child = node

    while ancestor and child is ancestor.right:
        child = ancestor
        ancestor = child.parent

    return ancestor.value if ancestor else None


root = Node(3)
root.parent = None
root.left = node1 = Node(1)
node1.parent = root
root.left.right = node2 = Node(2)
node2.parent = node1
root.right = node5 = Node(5)
node5.parent = root
root.right.left = node4 = Node(4)
node4.parent = node5
root.right.right = node6 = Node(6)
node6.parent = node5

print(root)

print(f"{successor(root) = } == ", 4)
print(f"{successor(node1) = } == ", 2)
print(f"{successor(node2) = } == ", 3)
print(f"{successor(node4) = } == ", 5)
print(f"{successor(node5) = } == ", 6)
print(f"{successor(node6) = } == ", None)
