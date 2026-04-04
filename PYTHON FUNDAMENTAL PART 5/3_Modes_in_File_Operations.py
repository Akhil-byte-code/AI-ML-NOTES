#  file operations 
# Modes 
# r reading (default )
# w  writing , truncates file first --> overwrite 
# x creates new & open for writing 
# a  writing , appends at end 
# b  binary mode 
# t   text mode (default )
# +  opens disk file for update(r & w)

# f = open("Sample3.txt" , "a")  # file obejct 
# f.write("New text being append \n to the file")
# f.close()

# we want to create a file Sample3_1.txt
# f = open("Sample3_1.txt" , "x")  # file object 
# f.write("Some random text") 
# f.close()

# diffrence between x and w 
# if file alredy exists then w will trucate the text and x will show u error 


# rt for reading in text ,ode and rb inbinary mode 
# wt write in text form and wb write in binary mode 
# r+ mreans we can perform read and write both
# w+ write along with oveeride  


# f= open("Sample3.txt" , "r+")  # file object  it add text at the starting  

# f.write("123")
# print(f.read())

# f.close()

# append 
# f= open("Sample3.txt" , "a+")  # file object  it add text at the end  

# f.write("123")
# print(f.read())  # nothing is displayed in the terminal bz our pointer is at the end 

# f.close()

# write + 
f= open("Sample3.txt" , "w+")  # file object  it oveerides the text 

f.write("123")
print(f.read())  # nothing is displayed in the terminal bz our pointer is at the end 

f.close()