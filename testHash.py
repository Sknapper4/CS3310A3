from firstHashMap import HashMap

h = HashMap(5)

h.create_hash_map()

h.add_new_object(['Beans', 1.85])
h.add_new_object(['fives', 1.85])
print(h.hash_map)

h.delete_object(['Beans', 1.85])
print(h.hash_map)

h.add_new_object(['Beans', 1.85])
print(h.hash_map)
