# Methods 
# instance , class & static methods 

#   instance                class           static 
# 1 1st parameter     1- 1st para (class) 1-no compulary para
# 2 access the class    2- access class    self x  cls x
#  & instance attributes   attributes     2-instance x class x
                        #   3- decorators 3-@staticmethod 
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
    
    @staticmethod
    def calc_discount(price , discount):
        final_price = price-(discount*price/100)
        print(f"discounted price = {final_price}")

l1 = Laptop("16gb" , "512gb")
# l2 = Laptop("8gb" , "256gb")

# l1.get_info()
# l1.get_storage_type()
# print(Laptop.get_storage_type())
l1.calc_discount(40_000 , 10)
