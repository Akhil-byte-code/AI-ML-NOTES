# Python Set Methods

#     s.add(val)     # adds a value
#     s.remove(val)   # removes a value
#     s.clear()     # empties the set
#     s.pop()      # removes a random value
#     s.union(set2)   # returns a new union
#     s.intersection(set2)

s={1,2,2,2,3}

# s.add(5)
# print(s)
# s.remove(1)
# print(s)
# s.clear()
# print(s)

# print(s)
# s.pop()
# print(s)

set1 = {3,4,5}
# s.union(set1)
print(s.union(set1))  #{1, 2, 3, 4, 5}
print(s.intersection(set1))