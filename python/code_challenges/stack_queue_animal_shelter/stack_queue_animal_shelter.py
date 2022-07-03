from python.code_challenges.data_structures.stacks_and_queues.queue import Queue


class AnimalShelter:
    def __init__(self, front=None, rear=None):
        self.front = front
        self.rear = rear

    def enqueue(self, animal):

        if self.front is None:
            self.front = animal
        else:
            self.rear.next = animal
        self.rear = animal

    def dequeue(self, preference):

        if self.front.value == preference:
            temp = self.front
            self.front = temp.next
            return temp

        elif self.front.value != preference:
            current = self.front
            while current:
                if current.value == preference:
                    return current
                self.front = current.next
                self.enqueue(current)
                print(current.value)
                current = current.next

        else:
            print('sorry out of that animal')

    def print(self):
        current = self.front
        while current:
            print(current.value)
            current = current.next


class Dog:
    def __init__(self):
        self.value = 'dog'
        self.next = None


class Cat:
    def __init__(self):
        self.value = 'cat'
        self.next = None


if __name__ == '__main__':
    shelter = AnimalShelter()
    cat1 = Cat()
    cat2 = Cat()
    dog = Dog()
    cat3 = Cat()
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)
    shelter.enqueue(dog)
    shelter.enqueue(cat3)
    shelter.dequeue('dog')
    shelter.print()
