# Intersection; Given two (singly) linked lists, determine if the two lists
# intersect. Return the inter- secting node. Note that the intersection is
# defined based on reference, not value. That is, if the kth node of the first
# linked list is the exact same node (by reference) as the j t h node of the
# second linked list, then they are intersecting.

# 💡
# Acá la solución sale sola si dibujás las listas intersecadas:
# A partir del nodo intersección, la cola de ambas listas coincide.
# Pero vos tenés ambas cabezas y no conocés el largo. Así que necesariamente
# tenés que recorrer ambas una vez para obtener el largo1 y largo2.
# Luego avanzás la diferencia en la lista más corta, y avanzás sincronizadamente
# a partir de ahí, comparando el nodo cada vez. El primero que coincida es
# la intersección.


from linked_list_jm import LinkedList, LinkedListNode


def get_length(head: LinkedListNode) -> int:
    node = head
    n = 0
    while node:
        n += 1
        node = node.next
    return n


def intersection(head1: LinkedListNode, head2: LinkedListNode) -> LinkedListNode:
    length1 = get_length(head1)
    length2 = get_length(head2)
    len_diff = abs(length1 - length2)

    node1, node2 = head1, head2
    # Advance the longest list len_diff steps
    for _ in range(len_diff):
        if length1 > length2:
            node1 = node1.next
        elif length2 > length1:
            node2 = node2.next

    # Now both lists are the same length. If they intersect, the interecting
    # node will be one of the remaining nodesn necessarily.
    for _ in range(min(length1, length2)):
        if node1 is node2:
            return node1  # or node2, they are the same!
        node1 = node1.next
        node2 = node2.next

    return None


ll1 = LinkedList(1, 2, 3, 4, 5, 6)
node4 = ll1.head.next.next.next

head2 = LinkedListNode(6)
head2.next = LinkedListNode(5)
head2.next.next = node4

# 1 -> 2 -> 3 -> 4 -> 5 -> 6
#      6 -> 5 -> ^

print(intersection(ll1.head, head2))

ll2 = LinkedList(1, 2, 3)

print(intersection(ll1.head, ll2.head))
