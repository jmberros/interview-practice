# Queue via Stacks: Implement a MyQueue class which implements a queue using two
# stacks.

# 💡
# Acá el truco es usar un stack como apoyo temporal cada vez que agregás un
# elemento nuevo, de modo de agregarlo al COMIENZO de la lista (al fondo del stack).
# Para esto tenés que popear todo, poner el nuevo, y despopear todo de regreso.

# NOTE:
# - Queue is FIFO
# - it can `add` (to the front) and `poll` (from the tail)

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def add(self, value: int):
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        self.stack2.append(value)  # Last value!
        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def poll(self) -> int:
        return self.stack1.pop()

    def __str__(self):
        return f"{self.stack1 = }, {self.stack2 = }"


q = MyQueue()

q.add(1)
print(q)
q.add(2)
print(q)
q.add(3)
print(q)

assert q.poll() == 1
print(q)
assert q.poll() == 2
print(q)

q.add(4)
print(q)

assert q.poll() == 3
print(q)
assert q.poll() == 4
print(q)
