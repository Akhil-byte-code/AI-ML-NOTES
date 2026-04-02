# Sets (immutable) unordered 
# collection of unique elements 

s={1,2,2,2,3}

print(len(s)) #3 it don't count duplicate element 

s.add(6)  # to add elemtn 
print(s)

empty_set = {} # it will create empty dict not set 
print(type(empty_set))

empty_set1 = set()
print(type(empty_set1))