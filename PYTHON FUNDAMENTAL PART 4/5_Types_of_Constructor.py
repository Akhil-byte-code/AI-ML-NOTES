class Student:
    def __init__(self):
        print("obj is beoing created ")
        
    def __init__(self , name , cgpa): # parametriced const 
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa
    
stu1 = Student("Rahul",9.0)
stu2 = Student("Akhil",9.2)
stu3 = Student("Amit",8.0)

print(f"{stu1.get_cgpa()} has name {stu1.name}")