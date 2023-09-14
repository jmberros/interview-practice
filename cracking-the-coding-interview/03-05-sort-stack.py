# Sort Stack: Write a program to sort a stack such that the smallest items are
# on the top. You can use an additional temporary stack, but you may not copy
# the elements into any other data structure (such as an array). The stack
# supports the following operations: push, pop, peek, and isEmpty.

# 💡
# Acá el orden sí o sí tiene que ser mantenido en cada PUSH operation.
# Al agregar un elemento, se compara con el top of the stack y se va popeando
# y storeando en el stack temporario hasta que el nuevo elemento puede ser
# introducido sin alterar el orden creciente.
# luego se popea back al stack original todos los temporalmente apartados.

# s = []
# t = []

# Push 2
# s = [2]
# t = []

# Push 1
# s = [2, 1]
# t = []


# Push 3
# while 3 > s.peek():
#    t.push( s.pop() )
# s.push(3)
# while t:
#    s.push( t.pop() )

# s = []
# t = [1, 2]
#
# s = [3]
# t = [1, 2]
#
# s = [3, 2, 1]
# t = []

class SortStack:
    def __init__(self):
        self.s = []
        self.t = []

    def push(self, value: int):
        while self.s and value > self.s[-1]:
            self.t.append(self.s.pop())
        self.s.append(value)
        while self.t:
            self.s.append(self.t.pop())

    def pop(self) -> int:
        return self.s.pop()


ss = SortStack()
for n in [1, 50, 10, 5, 3, 7, 9, 100, 64]:
    ss.push(n)
    print(ss.s)  # Should always be sorted in descending order
