# Stack Min: How would you design a stack which, in addition to push and pop,
# has a function min which returns the minimum element? Push, pop, and min
# should all operate in O(1) time.

# push 7 => [7] min [7]
# push 5 => [7, 5] min [7, 5]
# push 10 => [7, 5, 10] min [7, 5]
# push 1 => [7, 5, 10, 1] min [7, 5, 1]
# pop 1 => [7, 5, 10] min 5 [7, 5]


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    @property
    def min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return float("inf")

    def push(self, value: int):
        self.stack.append(value)
        if value <= self.min:
            self.min_stack.append(value)

    def pop(self) -> int:
        popped_value = self.stack.pop()
        if popped_value == self.min:
            self.min_stack.pop()


ms = MinStack()
ms.push(7)
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.push(5)
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.push(10)
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.push(1)
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.pop()
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.pop()
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
ms.pop()
print(f"{ms.stack = }, {ms.min = }, {ms.min_stack = }")
