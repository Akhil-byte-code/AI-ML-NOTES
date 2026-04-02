# Dictionary 
# key:value pairs 
#  |_ unique 

info = {
    "name":"akhil",
    "cgpa":9.5,
    "subjects":["maths" , "science"],
    3.14:"abc" # also posiible 
}

print(info)
print(type(info))
print(info["name"])
print(info[3.14])
info["cgpa"] = 10
# by nature mutable 
# unique keys  always and unordered 
