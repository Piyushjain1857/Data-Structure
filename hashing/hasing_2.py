# Hash table with chaining
hash_table = [[] for _ in range(10)]

def hash_function(key):
    return key % 10

def insert(key, value):
    index = hash_function(key)
    hash_table[index].append((key, value))

def search(key):
    index = hash_function(key)
    for k, v in hash_table[index]:
        if k == key:
            return v
    return None

# Usage
insert(15, "Apple")
insert(15, "Banana")  # no overwrite

print(search(15))   # Apple
print(search(15))  # Banana 
print(hash_table)  # [[(15, 'Apple'), (15, 'Banana')], [], [], [], [], [], [], [], [], []]

# Python dictionary (best and easiest)
hash_map = {}

hash_map[15] = "Apple"
hash_map[15] = "Banana"

print(hash_map[15])  # Banana