from python.code_challenges.data_structures.stacks_and_queues.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_shelter = Queue()
        self.cat_shelter = Queue()

    def enqueue(self, animal):
        if animal.value == 'dog':
            self.dog_shelter.enqueue(animal)
        elif animal.value == 'cat':
            self.cat_shelter.enqueue(animal)
        else:
            return 'please dont leave an animal, they need lovies!!'

    def dequeue(self, animal):
        if animal == 'dog':
            self.dog_shelter.dequeue()
        elif animal == "cat":
            return self.cat_shelter.dequeue()


class Dog:
    def __init__(self):
        self.value = 'dog'


class Cat:
    def __init__(self):
        self.value = 'cat'


if __name__ == '__main__':
    shelter = AnimalShelter()
    cat = Cat()
    print(cat)
    print(cat)
    shelter.enqueue(cat)
    print(shelter.dequeue('cat'))


