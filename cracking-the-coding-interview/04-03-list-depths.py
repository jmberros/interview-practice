# List of Depths: Given a binary tree, design an algorithm which creates a
# linked list of all the nodes at each depth (e.g., if you have a tree with
# depth D, you'll have D linked lists).

from binarytree import tree, Node
from collections import deque


class LinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __repr__(self):
        s = ""
        node = self
        while node:
            s += f"{node.value}->"
            node = node.next
        return s


def list_of_depths(root: Node) -> list[LinkedListNode]:
    queue = deque([root])  # A queue of BT Nodes
    linked_lists = []

    while queue:
        linked_list_last_node = None
        for i in range(len(queue)):
            bt_node = queue.popleft()
            linked_list_node = LinkedListNode(bt_node.value)
            if i == 0:
                linked_lists.append(linked_list_node)
            else:
                linked_list_last_node.next = linked_list_node
            linked_list_last_node = linked_list_node

            if bt_node.left:
                queue.append(bt_node.left)
            if bt_node.right:
                queue.append(bt_node.right)

    return linked_lists


root = tree(4)
print(root)
linked_lists = list_of_depths(root)

for ll in linked_lists:
    print(ll)
