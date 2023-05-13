class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)
        node = self.table[index]

        # If the slot is empty, create a new node and add it to the table
        if node is None:
            self.table[index] = Node(key, value)
        else:
            # If the slot is not empty, traverse the linked list and update the value if the key already exists
            while node.next is not None and node.key != key:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    def get(self, key):
        index = self.hash_function(key)
        node = self.table[index]

        # Traverse the linked list and return the value if the key is found
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next

        # If the key is not found, raise a KeyError
        raise KeyError(str(key))
