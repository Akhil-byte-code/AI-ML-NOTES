# Nesting 

username = input("enter usename ")
password = input("enter password ")

if (username=="admin" and password=="pass"):
    print("success")
else:
    if(username!="admin"):
        print("Wrong username")
    else:
        print("Wrong password")
    
# we can't write indvidual else and elif condition these are always used by if 
# we can use if condition individual 