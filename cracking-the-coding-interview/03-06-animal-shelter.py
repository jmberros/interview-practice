# Animal Shelter: An animal shelter, which holds only dogs and cats, operates on
# a strictly "first in, first out" basis. People must adopt either the "oldest"
# (based on arrival time) of all animals at the shelter, or they can select
# whether they would prefer a dog or a cat (and will receive the oldest animal
# of that type). They cannot select which specific animal they would like.
# Create the data structures to maintain this system and implement operations
# such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the
# built-in LinkedList data structure.

from linked_list_jm import LinkedList

# 💡
# usas dos Linked Lists: una de gatos y otra de perros, así tenes O(1) para quitar
# la head de cada lista, que sería el animal más "viejo"
# para dequeueAny, comparás las dos heads y ves cuál es más viejo
# para esto es necesario entonces un counter *general* del animal shelter,
# y a cada nuevo animal hay que ponerle el valor incrementado de ese counter


# Time: O(1) enqueue and dequeue
class AnimalShelter:
    def __init__(self):
        self.cats = LinkedList()
        self.dogs = LinkedList()
        self.counter = 0

    def enqueue(self, animal_type: str):
        """Enqueues an animal in their respective animal type queue."""
        self.counter += 1
        if animal_type == "C":
            self.cats.add(self.counter)
        elif animal_type == "D":
            self.dogs.add(self.counter)
        else:
            raise Exception(f"We don't accept this animal type: {animal_type}")

    def dequeue(self, animal_type: str) -> int:
        if animal_type == "C":
            linkedlist = self.cats
        elif animal_type == "D":
            linkedlist = self.dogs

        chosen_animal = linkedlist.head
        linkedlist.head = chosen_animal.next
        return chosen_animal.value

    def dequeueDog(self) -> int:
        """Pops the oldest dog."""
        return "D", self.dequeue(animal_type="D")

    def dequeueCat(self) -> int:
        """Pops the oldest cat."""
        return "C", self.dequeue(animal_type="C")

    def dequeAny(self) -> tuple[str, int]:
        """Pops the oldest animal of any kind."""
        next_cat = self.cats.head
        next_dog = self.dogs.head
        if not next_dog:
            return "C", self.dequeueCat()
        if not next_cat:
            return "D", self.dequeueDog()

        if next_cat.value < next_dog.value:
            return "C", self.dequeueCat()
        else:
            return "D", self.dequeueDog()


# Enqueue Cat C1
# Enqueue Cat C2
# Enqueue Dog D3
# Enqueue Cat C4
# Enqueue Dog D5
# Enqueue Cat C6

# cats = [D3 -> D5]
# dogs = [C1 -> C2 -> C4 -> C6]


shelter = AnimalShelter()
shelter.enqueue("C")
shelter.enqueue("C")
shelter.enqueue("D")
shelter.enqueue("C")
shelter.enqueue("D")
shelter.enqueue("C")

for i in range(shelter.counter):
    print(f"{shelter.cats = }")
    print(f"{shelter.dogs = }")
    print(f"Pop {i} : {shelter.dequeAny()}")

shelter.enqueue("C")
shelter.enqueue("C")
shelter.enqueue("C")
shelter.enqueue("D")

print(shelter.dequeueDog())
print(f"{shelter.cats = }")
print(f"{shelter.dogs = }")
