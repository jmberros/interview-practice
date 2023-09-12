# Three in One: Describe how you could use a single array to implement three
# stacks.


# NOTE: We need to assume a maximum capacity for the k stacks!

class EmptyStackException(Exception):
    pass


class FullStackException(Exception):
    pass


class MultiStack:
    def __init__(self, k: int, capacity: int):
        self.k = k
        self.capacity = capacity
        self.array = [None] * self.k * self.capacity
        self.sizes = [0] * self.k

    def pop(self, i: int) -> int:
        """Pops an element from the ith stack."""
        if self.sizes[i] == 0:
            raise EmptyStackException
        j = i * self.capacity + self.sizes[i] - 1
        value = self.array[j]
        self.array[j] = None
        self.sizes[i] -= 1
        return value

    def push(self, value: int, i: int):
        """Pushes a value to the ith stack."""
        if self.sizes[i] == self.capacity:
            raise FullStackException
        j = i * self.capacity + self.sizes[i]
        self.array[j] = value
        self.sizes[i] += 1

    def peek(self, i: int):
        """Peeks the top value of the ith stack."""
        j = i * self.capacity + self.sizes[i] - 1
        return self.array[j]

    def __str__(self):
        return repr(self.array)


ms = MultiStack(k=3, capacity=2)
ms.push(1, 0)
print(ms)
ms.push(2, 0)
print(ms)
ms.push(-1, 2)
print(ms)
ms.push(-2, 2)
print(ms)
ms.push(10, 1)
print(ms)
ms.push(20, 1)
print(ms)

assert ms.pop(0) == 2
print(ms)
assert ms.pop(2) == -2
print(ms)
assert ms.pop(0) == 1
print(ms)

ms.pop(0)  # Should raise EmptyStack
