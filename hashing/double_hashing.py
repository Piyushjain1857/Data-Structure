class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def h1(self, key):
        return key % self.size

    def h2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key, value):
        index = self.h1(key)
        i = 0

        while self.table[(index + i * self.h2(key)) % self.size] is not None:
            i += 1

        self.table[(index + i * self.h2(key)) % self.size] = (key, value)

    def search(self, key):
        index = self.h1(key)
        i = 0

        while self.table[(index + i * self.h2(key)) % self.size] is not None:
            k, v = self.table[(index + i * self.h2(key)) % self.size]
            if k == key:
                return v
            i += 1
            if i == self.size:
                return None
        return None
    
# Example usage:
hash_map = DoubleHashing(10)
hash_map.insert(3, "One")
hash_map.insert(33, "Eleven")   
hash_map.insert(23, "Two")

# print(hash_map.search(1))   
# print(hash_map.search(11))  
# print(hash_map.search(2)) 
for i in range(10):
    print(hash_map.table[i])