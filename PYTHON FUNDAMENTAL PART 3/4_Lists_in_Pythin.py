# Lists 
# mutable sequence of values 

# marks1 = 90
# marks2 = 100
# marks3 = 98
# marks4 = 90
# marks5 = 90
# to avoid this we use list 
# marks = [99,90,100,56,78]
marks = [99,90,100,56,78,"abc"]

marks[3] = 57
print(marks)

# Slicing in list (sublist)
# list[start idx :end idx (not included )]
print(marks[0:5])
print(marks[5:len(marks)])


