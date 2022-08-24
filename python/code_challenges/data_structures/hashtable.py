from linked_list.linked_list import LinkedList

class Hashtable:
    def __init__(self, size=10):
        self.size = size
        self.buckets = size * [None]
   
    def hash(self, key):
        # method body here
        total = 0

        for ch in key:
            total += ord(ch)

        primed = total * 19

        index = primed % self.size
        return index

    def set(self,key, value):
        index = self.hash(key)
        if self.buckets[index] == None:
            new_linked = LinkedList()
            new_linked.insert({key:value})
            self.buckets[index] = new_linked
        else:
            self.buckets[index].insert({key:value})
        


    def get(self, key):
        index = self.hash(key)
        if self.buckets[index]:
            return self.buckets[index].head.value[key]

    def contains(self,key):
        index = self.hash(key)
        if self.buckets[index]:
            current = self.buckets[index].head
            while current:
                keysList = list(current.value.keys())
                if keysList[0] == key:
                    return True
                current = current.next
                
            return False
        else:
            return False
            


    def keys(self):
        keys_list = []
        for linked_list in self.buckets:
            if linked_list is not None:
                current = linked_list.head
                while current:
                    keys = list(current.value.keys())
                    keys_list.append(keys[0])
                    current = current.next
        return keys_list  

if __name__ == '__main__':
    new_table = Hashtable()
    new_table.set('tad', 'hampton')
    new_table.set('dat', 'hampton')
    new_table.set('brendon', 'lee')
    new_table.set('brendon', 'fdgdfg')
    new_table.set('browdbf', 'lee')
    # print(new_table.contains(''))
    print(new_table.keys())
