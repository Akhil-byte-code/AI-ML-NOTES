# tuple is a immuutable sequence of values  datatypes 

# tup =(1,2,3,4,5)
tup =(1,2,3,4,5,"abc", 3.14)
# tup[3] = 67 shows error 

print(tup)
print(type(tup))
print(len(tup))

# we can write list 
lis = [3]
print(type(lis))
# but we can't write 
# tup = (1)
# tup = ("abc") # string 

print(type(tup)) # it is treated as int 
# slicing 
# for full 
print(tup[:])
