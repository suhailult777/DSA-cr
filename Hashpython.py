class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size
    
    def put(self, key, value):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                entry[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for entry in self.table[index]:
            if entry[0] == key:
                return entry[1]
        raise KeyError(key)

    def display_hashes(self):
        for index, bucket in enumerate(self.table):
            for key, _ in bucket:
                print(f"Key: {key}, Hash: {self._hash(key)}, Index: {index}")

# Example use cases

hash_table = HashTable(size=10)

    
# Add key-value pairs
hash_table.put("apple", 111)
hash_table.put("banana", 123)
hash_table.put("cherry", 147)
hash_table.put("pears", 145)
hash_table.put("watermelon", 120)
hash_table.put("grapes", 167)
hash_table.put("blackberry", 777)

# Retrieve values
print(hash_table.get("apple"))   # Output: 111
print(hash_table.get("banana"))  # Output: 123

# Update a value
hash_table.put("apple", 150)
print(hash_table.get("apple"))  # Output: 150

# Display hash values
hash_table.display_hashes()



