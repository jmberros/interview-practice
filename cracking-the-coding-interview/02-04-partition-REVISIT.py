# Partition: Write code to partition a linked list around a value x, such that
# all nodes less than x come before all nodes greater than or equal to x. Ifxis
# contained within the list, the values of x only need to be after the elements
# less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right
# partitions.

# Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
# [partition=5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linked_list_jm import LinkedList, LinkedListNode


def partition(head: LinkedListNode, x: int) -> LinkedListNode:
    node = head
    prev_node = None
    while node:
        next_node = node.next
        if node.value < x and node != head:
            prev_node.next = next_node
            node.next = head
            head = node
            print(f"New head {head.value}")
        else:
            prev_node = node
        node = next_node

    return head


ll = LinkedList(3, 5, 8, 5, 10, 1, 2)
print(ll)
ll = LinkedList.init_from_head(partition(ll.head, 5))
print(ll)
