# class MyHashMap:
#     def __init__(self):
#         self.map = {}

#     def put(self, key, value):
#         self.map[key] = value

#     def get(self, key):
#         return self.map.get(key, -1)

#     def remove(self, key):
#         if key in self.map:
#             del self.map[key]
            
# # Example usage:
# hash_map = MyHashMap()
# hash_map.put(1, 1)
# hash_map.put(2, 2)
# print(hash_map.get(1))  # returns 1
# print(hash_map.get(3))  # returns -1 (not found)
# hash_map.put(2, 1)      # update the existing value
# print(hash_map.get(2))  # returns 1
# hash_map.remove(2)      # remove the mapping for 2
# print(hash_map.get(2))  # returns -1 (not found)        

