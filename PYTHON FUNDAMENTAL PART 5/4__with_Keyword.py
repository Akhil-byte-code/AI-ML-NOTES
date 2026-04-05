# with keyword 
# with open("data.txt","r") as f :
#   print(f.read())
# it is used to automatcially close the file after all operations are pefomred 

with open("Sample4.txt" , "r") as f:
    data = f.read()
    # print(f.read())
    print(len(data))