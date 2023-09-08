from collections.abc import Iterable
from typing import List, Optional


class LinkedListNode:
    def __init__(self, value: int):
        self.value = value
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.value)
        # rep = str(self.value)
        # if self.prev is not None:
        #     rep = ":" + rep
        # if self.next is not None:
        #     rep += ":"
        # return rep


class LinkedList:
    # TODO Docstring to the class and to all methods

    @staticmethod
    def merge(left, right):
        left.tail.next = right.head
        right.head.prev = left.tail
        return left

    def __init__(self, *values: List[int]):
        self.head = None
        self.tail = None

        if len(values) == 1 and isinstance(values[0], Iterable):
            values = values[0]

        if values:
            for value in values:
                self.add(value)

    @classmethod
    def init_from_head(cls, head: LinkedListNode):
        values = []
        node = head
        while node:
            values.append(node.value)
            node = node.next
        return cls(values)

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    def __len__(self):
        return sum(1 for node in self)

    def is_empty(self):
        return self.head is None and self.tail is None

    def one_item_list(self):
        return self.head == self.tail

    def add(self, value: int):
        n = LinkedListNode(value)
        if self.head is None:
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n

    def delete(self, value: int):
        n = self.head

        if n is None:
            return

        if n.value == value:
            self.head = n.next  # Head shifts

        while n.next is not None:
            if n.next.value == value:
                n.next = n.next.next  # Skip a node
            n = n.next

    def find(self, value: int) -> Optional[LinkedListNode]:
        for node in self:
            if node.value == value:
                return node

    def move_node_to_head(self, node: LinkedListNode):
        if self.head is None:
            self.add(node)
            return
        if self.head == node:
            return

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head

        self.head.prev = node
        self.head = node

    def prepend(self, value: int):
        self.move_node_to_head(LinkedListNode(value))

    def reverse_iter(self):
        current = self.tail
        while current is not None:
            yield current
            current = current.prev

    def reverse(self):
        current = self.tail
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.next

        self.tail, self.head = self.head, self.tail

    def __repr__(self):
        n = self.head
        values = []
        while n is not None:
            values.append(str(n))
            n = n.next
            if len(values) > 20:  # Guard for circularities
                break
        return "LinkedList(" + "-".join(values) + ")"

    def __eq__(self, other):
        return repr(self) == repr(other)  # Hack
