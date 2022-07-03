from python.code_challenges.data_structures.stacks_and_queues.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.dog_shelter = Queue()
        self.cat_shelter = Queue()

    def enqueue(self, animal):
        if animal == 'Dog':
            dog = Dog()
            self.dog_shelter.enqueue(dog.value)
        if animal == 'Cat':
            cat = Cat()
            self.cat_shelter.enqueue(cat.value)
        else:
            return 'please dont leave an animal, they need lovies!!'


class Dog:
    def __init__(self):
        self.value = 'Dog'
        self.next = None


class Cat:
    pass


if __name__ == '__main__':
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue('Dog')
    print(animal_shelter.dog_shelter.front.value)
