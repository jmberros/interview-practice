# Sum Lists: You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that the
# Vs digit is at the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.

# 💡
# Para este necesitás el largo de ambos números, así que hay que recorrer
# ambas listas una vez.
# Luego las "alineás" avanzando la más larga un número de pasos igual a la
# diferencia de largo. Vas sumando el número * 10^i, donde i ahora empieza desde
# n - 1 y va bajando (n = nodos en la más larga)
# Acá no hace falta carry over.

# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).Thatis,617 + 295
# Output: 9 -> 1 -> 2, That is, 912.

# 1 0 9 5 length 4
#   1 2 5 length 3
# 1 2 2 0
#
# i = 3
# total = 1000
# i = 2
# 0
# 1
# total = 1000 + 100 = 1100
# i = 1
# 9
# 2
# total = 1100 + 110 = 1210
# i = 0
# 5
# 5
# total = 1210 + 10 = 1220

from linked_list_jm import LinkedList, LinkedListNode


def get_length(head: LinkedListNode) -> int:
    node = head
    n = 0
    while node:
        n += 1
        node = node.next
    return n


def sum_lists_2(head1: LinkedListNode, head2: LinkedListNode) -> int:
    length1 = get_length(head1)
    length2 = get_length(head2)
    len_diff = abs(length1 - length2)

    exp = max(length1, length2) - 1
    total = 0
    node1, node2 = head1, head2

    # Advance the longest list len_diff steps
    for i in range(len_diff):
        if length1 > length2:
            total += node1.value * 10**exp
            node1 = node1.next
        elif length2 > length1:
            total += node2.value * 10**exp
            node2 = node2.next
        exp -= 1

    # We have now equal number of remaining nodes in both lists
    while node1 and node2:
        total += (node1.value + node2.value) * 10**exp
        node2 = node2.next
        node1 = node1.next
        exp -= 1

    assert exp == -1
    assert node1 is None and node2 is None

    return total


head1 = LinkedList(6, 1, 7).head
head2 = LinkedList(2, 9, 5).head

head1 = LinkedList(1, 0, 9, 6).head
head2 = LinkedList(2, 9, 5).head

total = sum_lists_2(head1, head2)
print(total)
