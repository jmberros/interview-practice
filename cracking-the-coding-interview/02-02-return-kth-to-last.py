# Return Kth to Last: Implement an algorithm to find the kth to last element of
# a singly linked list.


from linked_list_jm import LinkedList, LinkedListNode

test_cases = [
    (dict(head=[1, 2, 3, 4, 5], k=2), [4, 5]),
    (dict(head=[1, 2, 3, 4, 5], k=3), [3, 4, 5]),
]


# NOTE: Uses a hashmap to store nodes
# Time: O(n)
# Space: O(n)
def return_kth_to_last(head: LinkedListNode, k: int) -> LinkedListNode:
    """Returns the Kth to last element of the list."""
    nodes = {}

    i = 1
    node = head
    while node:
        nodes[i] = node
        node = node.next
        i += 1

    n = i  # Last value of i is the number of nodes
    return nodes[n - k] if k <= n else None


# NOTE: Two pointers trick
# Time: O(n)
# Space: O(1)
def return_kth_to_last_2(head: LinkedListNode, k: int) -> LinkedListNode:
    p1, p2 = head, head

    # (1) Advance p1 k steps
    n = 0
    while n < k:
        if not p1:
            return None  # list has less than k elements
        p1 = p1.next
        n += 1

    # (2) Advance p1 and p2 in tandem until p1 hits the end
    while p1.next:
        p1 = p1.next
        p2 = p2.next

    # (3) Now p2 sits in the kth to last element
    return p2


if __name__ == "__main__":
    for inp, exp in test_cases:
        out = return_kth_to_last(LinkedList(inp["head"]).head, inp["k"])
        out = LinkedList.init_from_head(out)
        print(inp)
        print(exp)
        print(repr(out))
