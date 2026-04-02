info = {
    "name":"akhil",
    "cgpa":9.5,
    "subjects":["maths" , "science"],
    3.14:"abc" # also posiible 
}

# dict_keys = info.keys()  # simple 
# dict_keys = list(info.keys()) # list type 
# dict_values = list(info.values())

# print(dict_keys)
# print(type(dict_keys))
# print(dict_values)

# d.keys()  # returns all keys 
# d.values()  #return all values 
# d.items()  # returns (key , val) pairs 
# d.get(val)  #returns val acc. to  key 
# d.update(new_item)  # add new items to dict 
# dict[value]  it will show an error if val not found but dict[get(val)] wil not show an error 

# print(info.get("cgpa"))
# # print(info.["cgpa2"])  # it will show an error 
# print(info.get("cgpa2")) # it simply print none and below code run properly 
# print("End of code ")

info.update({
    "city":"Delhi"
})

print(info)
