# type Conversion 

# int --> float 
# float --> int 
# int --> bool 

#  "abc123"--> int 
#  "123" --> int(123)

# Type conversion(implicit)   and Type casting (explicit)

a = 10 
ans = 5 + 10.0
b = 5 
print(type(a/5))  # implicit 
print(type(ans))  # implicit 


# Type casting (explicit) --> we convert into complatible data type 
ans1 = int(5+10.0)  # casting
print(ans1 , type(ans1))

val = int("123")
print(type(val))

val1 = bool(10)
print(val , type(val1))


