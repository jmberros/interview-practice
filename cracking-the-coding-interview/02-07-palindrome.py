# Palindrome: Implement a function to check if a linked list is a palindrome.


from linked_list_jm import LinkedList, LinkedListNode


def get_length(head: LinkedListNode) -> int:
    node = head
    n = 0
    while node:
        n += 1
        node = node.next
    return n


def is_palindrome(head: LinkedListNode) -> bool:
    length = get_length(head)
    stack = []

    node = head
    for _ in range(length // 2):
        stack.append(node.value)
        node = node.next

    if length % 2 != 0:
        node = node.next

    for _ in range(length // 2):
        expected_value = stack.pop()
        if node.value != expected_value:
            return False
        node = node.next

    assert not stack

    return True


ll = LinkedList(3, 1, 2, 5, 2, 1, 3)
print(ll, is_palindrome(ll.head))

ll = LinkedList(3, 1, 2, 2, 1)
print(ll, is_palindrome(ll.head))
