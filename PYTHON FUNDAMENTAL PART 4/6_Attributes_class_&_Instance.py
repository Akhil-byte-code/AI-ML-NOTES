# Attributes 
# class & instance

#  class --> belong to class --> common 
# instance --> belong to object --> unique 
# Student --> name , subject , cgpa ---> instance 
# college name -> class  

class Student:
    college_name = "ABC college" # class attributes 
    PI = 3.14

    def __init__(self , name , cgpa):
        self.name = name # insntance 
        self.cgpa = cgpa
        self.PI = 3.14


stu1 = Student("Akhil" , 9.2) 

print(stu1.name)
print(stu1.college_name)
print(Student.college_name)
# when instance and class attributes are present with same name then instance have higher precendence 
print(Student.PI)