# Loop Detection: Given a circular linked list, implement an algorithm that
# returns the node at the beginning of the loop.


from linked_list_jm import LinkedList, LinkedListNode


# Is this solution cheating?
# Gayle implements a very annoying unintuitive solution
def return_looping_node(head: LinkedListNode) -> LinkedListNode:
    seen = set()
    node = head
    while node:
        if id(node) in seen:
            return node
        seen.add(id(node))
        node = node.next
    return None


ll = LinkedList(1, 2, 3)
node1 = ll.head
node2 = ll.head.next
node3 = ll.head.next.next
node3.next = node2

print(return_looping_node(ll.head))  # Should be 2
