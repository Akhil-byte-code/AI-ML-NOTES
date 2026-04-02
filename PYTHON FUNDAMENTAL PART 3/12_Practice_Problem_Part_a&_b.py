# Student Enrolment 
# Given a list of tuples with info(name , subject):
#     .list all unique course 
#     .list student enrolled in English 
#     .create dictionary (student , set of courses )

info ={
    ("Alice","Math"),
    ("Bob" , "Science"),
    ("Alice","Science"),
    ("Charle" , "Math"),
    ("Bob" , "Math"),
    ("Alice","English"),
    ("Charle" , "English"),
}

# # (i)
# unique_course = set()
# for tup in info:
#     # print(tup[0])  #name 
#     # print(tup[1]) #course 
#     unique_course.add(tup[1])

#  # or instead of using index 
# for name ,course in info:
#     print(name,course)


# print(unique_course)

# # (ii)
# for name , course in info:
#     if(course=="English"):
#         print(name)

# (iii)
for name ,course in info:
    if(dict.get(name)==None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)