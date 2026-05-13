# 📌 Hashing Notes (BCA - AI & Data Science)

## 🔹 1. Hashing Overview
Hashing is a technique used to map data (keys) to specific locations in a table using a **hash function**. It allows **fast data access (O(1) average time)**.

---

## 🔹 2. Hash Functions

### ✔ Definition:
A hash function takes an input (key) and returns an index (hash value).

### ✔ Properties:
- Deterministic (same input → same output)
- Fast computation
- Uniform distribution (avoid clustering)
- Minimizes collisions

### ✔ Example:
```python
def hash_function(key, size):
    return key % size
    
---

## 🔹 3. Hash Table

- Stores key-value pairs
- Uses array/list internally

---

## 🔹 4. Collision

When two keys map to same index → **Collision**

---

# 🔸 5. Collision Resolution Techniques

---

## 🔹 A. Chaining

### ✔ Concept:
Each index stores a **list**

---

# Simple hash table using list

hash_table = [None] * 10

def hash_function(key):
    return key % 10   # simple modulo hash

def insert(key, value):
    index = hash_function(key)
    hash_table[index] = value

def search(key):
    index = hash_function(key)
    return hash_table[index]

# Usage
insert(5, "Apple")
insert(15, "Banana")  # collision will overwrite

print(search(5))   # Apple
print(search(15))  # Banana
```
---

### ✔ Full Code (Insert, Search, Delete)

```python
class HashTableChaining:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        self.table[index].append(key)

    def search(self, key):
        index = self.hash(key)
        return key in self.table[index]

    def delete(self, key):
        index = self.hash(key)
        if key in self.table[index]:
            self.table[index].remove(key)

    def display(self):
        for i, val in enumerate(self.table):
            print(i, ":", val)
```

---

## 🔹 B. Open Addressing

### ✔ Concept:
Find another empty slot inside table

---

# 🔸 1. Linear Probing

```python
class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)

        while self.table[index] is not None:
            index = (index + 1) % self.size

        self.table[index] = key

    def search(self, key):
        index = self.hash(key)

        while self.table[index] is not None:
            if self.table[index] == key:
                return True
            index = (index + 1) % self.size

        return False

    def display(self):
        print(self.table)
```

---

# 🔸 2. Quadratic Probing

```python
class QuadraticProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash(key)
        i = 0

        while self.table[(index + i*i) % self.size] is not None:
            i += 1

        self.table[(index + i*i) % self.size] = key

    def search(self, key):
        index = self.hash(key)
        i = 0

        while self.table[(index + i*i) % self.size] is not None:
            if self.table[(index + i*i) % self.size] == key:
                return True
            i += 1

        return False

    def display(self):
        print(self.table)
```

---

# 🔸 3. Double Hashing

```python
class DoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash1(self, key):
        return key % self.size

    def hash2(self, key):
        return 1 + (key % (self.size - 1))

    def insert(self, key):
        h1 = self.hash1(key)
        h2 = self.hash2(key)

        i = 0
        while self.table[(h1 + i * h2) % self.size] is not None:
            i += 1

        self.table[(h1 + i * h2) % self.size] = key

    def search(self, key):
        h1 = self.hash1(key)
        h2 = self.hash2(key)

        i = 0
        while self.table[(h1 + i * h2) % self.size] is not None:
            if self.table[(h1 + i * h2) % self.size] == key:
                return True
            i += 1

        return False

    def display(self):
        print(self.table)
```

---

## 🔹 6. Comparison Table

| Feature | Chaining | Linear Probing | Quadratic Probing | Double Hashing |
|--------|----------|----------------|-------------------|----------------|
| Method | Uses list at index | Sequential search | Jump using i² | Uses second hash |
| Memory | Extra memory | No extra memory | No extra memory | No extra memory |
| Clustering | No | High | Less | Minimal |
| Performance | Good if small chains | Degrades | Better | Best |
| Complexity | Simple | Simple | Moderate | Complex |
| Deletion | Easy | Difficult | Difficult | Difficult |

---

## 🔹 7. Custom Hash Map using Python Dictionary

```python
class CustomHashMap:
    def __init__(self):
        self.map = {}

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        return self.map.get(key, "Not Found")

    def remove(self, key):
        if key in self.map:
            del self.map[key]

    def display(self):
        print(self.map)
```

---

## ✅ The End
