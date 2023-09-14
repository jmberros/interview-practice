# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too
# high, it might topple. Therefore, in real life, we would likely start a new
# stack when the previous stack exceeds some threshold. Implement a data
# structure SetOfStacks that mimics this. SetOfStacks should be composed of
# several stacks and should create a new stack once the previous one exceeds
# capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically
# to a single stack (that is, pop() should return the same values as it would if
# there were just a single stack).

# FOLLOW UP: Implement a function popAt(int index) which performs a pop
# operation on a specific sub-stack.

# 💡
# La clase lleva un array de stacks y otro de sizes, y agrega un nuevo stack
# al array cuando el size DEL ULTIMO es max capacity.
# Al popear se borran stacks vacío si los hubiera.


class EmptyStackException(Exception):
    pass


class SetOfStacks:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.sizes = []
        self.add_new_stack()  # Initializes the first stack

    @property
    def last_stack(self):
        return self.stacks[-1]

    @property
    def last_stack_size(self):
        return self.sizes[-1]

    @property
    def last_stack_is_full(self):
        return self.last_stack_size == self.capacity

    @property
    def last_stack_is_emtpy(self):
        return self.last_stack_size == 0

    def add_new_stack(self):
        self.stacks.append([])
        self.sizes.append(0)

    def remove_stack(self):
        if len(self.stacks) == 1:
            raise EmptyStackException  # Can't remove the only stack remaining
        self.stacks.pop()
        self.sizes.pop()

    def push(self, value: int):
        if self.last_stack_is_full:
            self.add_new_stack()
        self.sizes[-1] += 1
        self.last_stack.append(value)

    def pop(self) -> int:
        if self.last_stack_is_emtpy:
            self.remove_stack()
        self.sizes[-1] -= 1
        return self.last_stack.pop()

    def pop_at(self, i: int) -> int:
        if i > len(self.stacks) - 1:
            raise Exception(f"No stack with index {i}")
        if self.sizes[i] == 0:
            raise EmptyStackException
        self.sizes[i] -= 1
        return self.stacks[i].pop()


ss = SetOfStacks(capacity=2)
for i in range(10):
    ss.push(i)
    print(ss.stacks)

ss.pop_at(2)
print(ss.stacks)
ss.pop_at(1)
print(ss.stacks)

for i in range(11):
    ss.pop()
    print(ss.stacks)  # Should raise empty stack for the last pop
