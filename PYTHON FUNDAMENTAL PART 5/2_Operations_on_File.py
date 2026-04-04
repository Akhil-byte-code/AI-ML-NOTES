# File operations 
# Open , read & close 

# f = open("data.txt","r")
        #  filename  mode (read or write )
        #   path 

# create a sample file sample.txt
# f= open("Sample2.txt" , "r")  # file object return by this line 

# data = f.read()
# print(data)
# print(type(data))

# data1 = f.readline()  # readlines read the text as line by line 
# print(data1)

# data2 = f.readline()  # readlines read the text as line by line 
# print(data2)
# f.close()

f= open("Sample2.txt" , "w") 
f.write("Text to overwrite \n the complete data ")
f.close()

