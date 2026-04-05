# Word Search 
data = True
line = 1

# reading data line by line by using loop 
with open("Sample6.txt" , "r") as f :
    while data:
        data = f.readline()
        # to check if python is present or not 
        if ("Python" in data):
            print(f"Word found at line {line}")
            break

        print(data)
        line+=1