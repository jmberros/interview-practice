# Sum Lists: You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that the
# Vs digit is at the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.

from linked_list_jm import LinkedList, LinkedListNode


def sum_lists(head1: LinkedListNode, head2: LinkedListNode) -> int:
    # 7 -> 1 -> 6 == 617
    # 5 -> 9 -> 2 == 295

    previous_carry_over = 0
    total = 0
    i = 0
    node1, node2 = head1, head2
    while node1 or node2:
        value1 = node1.value if node1 else 0
        value2 = node2.value if node2 else 0
        carry_over, remainder = divmod(value1 + value2, 10)
        total += (remainder + previous_carry_over) * 10**i

        previous_carry_over = carry_over
        node1 = node1.next
        node2 = node2.next
        i += 1

    if previous_carry_over:
        total += previous_carry_over * 10**i

    return total


head1 = LinkedList(7, 1, 6).head
head2 = LinkedList(5, 9, 2).head

total = sum_lists(head1, head2)

print(total)
