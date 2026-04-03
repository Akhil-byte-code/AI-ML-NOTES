# Methods 
# instance , class & static methods 

#   instance                class           static 
# 1 1st parameter     1- 1st para (class)
# 2 access the class    2- access class  
#  & instance attributes   attributes
                        #   3- decorators
                        # @classmethod

class Laptop:
    storage_type = "sad"

    def __init__(self , RAM , storage):
        self.RAM = RAM
        self.storage = storage
    @classmethod   # decorators - it takes another input and change the behavior 
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type} {cls.RAM}")

    def get_info(self):
        print(f"Laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")

l1 = Laptop("16gb" , "512gb")
# l2 = Laptop("8gb" , "256gb")

# l1.get_info()
l1.get_storage_type()
print(Laptop.get_storage_type())
