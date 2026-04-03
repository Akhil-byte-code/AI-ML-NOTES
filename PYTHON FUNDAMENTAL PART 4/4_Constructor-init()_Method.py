# Constructor 
# _init_method --> create an obejct 

class Student:
    # def __init__(self):  #initialize one object 
        # print("this is the constructor ")
    def __init__(self,name):
        self.name = name


# self --> current instance of the class --> curr object 
# self(instance method) -> compulsory parameter 

stu1 = Student("Rahul")
stu2 = Student("Akhil")
stu3 = Student("Ankit")

print(stu1.name)
print(stu2.name)
print(stu3.name)


