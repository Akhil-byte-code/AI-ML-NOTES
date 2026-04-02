tup = [1,2,3,4,10]

sum =0

for val in tup:
    sum+=val

print(f"the sum of value is {sum}")

# tuple method 
# t.index(val)  # returns 1st occurence idx 
# t.count(val)  # counts total occurrence 

tup2 = (1,2,2,3,4,4,5)

print(tup2.count(2))
print(tup2.index(2))
