# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP How would you solve this problem if a temporary buffer is not
# allowed?

# 💡
# El problema es mucho más complicado si hay que remover TODOS los nodos
# de cada grupo de duplicados.
# Si el primero puede quedar, es fácil: vas registrando en un Hashmap los
# valores observados y si alguno ya fue observado antes, lo salteás
# (para esto necesitás ir trackeando el previous_node).


from linked_list_jm import LinkedListNode

test_cases = [
    ([1, 1, 1, 1], [1]),
    ([1, 2, 1, 2, 3, 1], [1, 2, 3]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
]


# Solution using temporary buffer?
# Time: O(n)
# Space: O(n)
def remove_dups(head: LinkedListNode) -> LinkedListNode:
    """Remove all duplicates from the linked list."""
    seen = set()
    prev_node = None
    node = head
    while node:
        if node.value in seen:
            prev_node.next = node.next
            # Keep prev_node as the previous node, don't update it in this case
        else:
            seen.add(node.value)
            prev_node = node

        node = node.next

    return head  # The head will never be a duplicate


# PENDING: Without a temporary buffer

if __name__ == "__main__":
    from helpers import run_test_cases_ll

    run_test_cases_ll(test_cases, remove_dups)
