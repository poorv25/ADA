class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        # If the slot is empty, add the key-value pair to the table
        if self.keys[index] is None:
            self.keys[index] = key
            self.values[index] = value
        else:
            # If the slot is not empty, linearly probe to find the next available slot
            i = (index + 1) % self.size
            while self.keys[i] is not None and self.keys[i] != key:
                i = (i + 1) % self.size

            # If the key already exists, update its value
            if self.keys[i] == key:
                self.values[i] = value
            else:
                # If an empty slot is found, add the key-value pair to the table
                self.keys[i] = key
                self.values[i] = value

    def get(self, key):
        index = self.hash_function(key)

        # Traverse the table linearly to find the key
        i = index
        while self.keys[i] is not None:
            if self.keys[i] == key:
                return self.values[i]
            i = (i + 1) % self.size
            if i == index:
                break

        # If the key is not found, raise a KeyError
        raise KeyError(str(key))
