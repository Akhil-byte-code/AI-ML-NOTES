# JSON Module (Javascriptobject notation)
# import json   
# {
#       "name":"Akhil"
#       "subject" :["Python" , "DataScience"]
# }

# . json.loads()(string) --> JSON string --> pyhton object
# .json.dumps()(store )
# .json.load() read   to deal with file don't use s and to deal with string s comes 
# .json.dump() write 

# import json 

# py_object = {
#     "name":"Akhil",
#     "isTeacher" :True
#     # "isTeacher" :None

# }

# # json_str = '{"name":"Akhil" , "isteacher":true }'
# json_string = json.dumps(py_object)
 
# #  to convert it into pyhton object 
# # py_object = json.loads(json_str)
# # print(type(json_str))
# print(type(json_string) , json_string)



import json

data = {
    "name" : "Akhil",
    "age" : 27, 
    "isTeacher":True
}


# with open("Data.json" , "r") as f :
with open("Data.json" , "w") as f :

    # py_obj =json.load(f)
    # json.dump(data , f)
    # json.dump(data , f , indent=4)
    json.dump(data , f , indent=4 , sort_keys=True)
    # print(type(py_obj))
# this will dump the pres=vious data 

