# List comprehension 
# [output for item in iterable if condition ]

squares = []

for i in range(6):
    squares.append(i*i)

print(squares)

# List comprehension 
# sq = [i*i for i in range(6)]  
sq = [i*i for i in range(6) if(i%2!=0)]  # by addingextra condition   
print(sq)

# to replace neg value witn 0 
nums = [-2 , -4 , 3 ,5 ,2 ,-1]
numsnew = [0 if val<0 else val for val in nums]
print(numsnew)

# to convert the value in uppercase 
words = ["hello" , "pyhton" , "akhil"]

words = [val.upper() for val in words]
print(words)