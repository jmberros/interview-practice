# Delete Middle Node: Implement an algorithm to delete a node in the middle
# (i.e., any node but the first and last node, not necessarily the exact middle)
# of a singly linked list, given only access to that node.

# 💡 Esto es medio una forrada, requiere pensar fuera de la caja:
# en vez de borrar literalmente ese nodo, que es imposible sin acceso al previo,
# copiás el valor del próximo a este y borrás el próximo. El efecto es el mismo!

from linked_list_jm import LinkedListNode

# Trick from the book! Move the values around, the "actual nodes" don't matter.
# 1 2 3 4 5 6 7
# DEL(5)
# 1 2 3 4 5<-6 7 copy the next value
# 1 2 3 4 6 6 7
# 1 2 3 4 6 X 7 remove the next node
# 1 2 3 4 6 7


def delete_node(node: LinkedListNode) -> LinkedListNode:
    """Delete a "middle" node (i.e. not first nor last)."""

    node.value = node.next.value
    node.next = node.next.next
