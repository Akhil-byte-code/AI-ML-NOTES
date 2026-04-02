# Strings 
# Formatting (dynamic  string )

# 1- format()-->py3 (placeholder {}  placement rate )
# 2- f-string 

a=5 
b=10
sum = a+b

# normal formatting 
print("langugae is {}".format("pyhton"))
print("sum is {}".format(sum))
print(" num one {} & {} and sum is {}".format(a,b,sum))

# index based formating 
print("sum of {1} & {0} is {2}".format(a,b,sum)) # here values are assiinged on the basis of index 

# value based formatting 
print("values of vars {a} & {b}".format(a=14,b=40))

# F-String (literal string inuterpretation)
# f"{variabl expression}"
print(f"sum of {a} & {b} is {a+b}")
print(f"avg of {a} & {b} is {(a+b)/2}")

