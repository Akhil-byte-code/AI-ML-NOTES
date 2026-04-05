# Exception handling 
# try , except , else , finally 
# the block of code which may cause exception is in the try block 

try:
    x=int(input("Enter x : "))
    ans = 10/x 
except ZeroDivisionError: # if exception throws then it run 
    print("Divide by 0 is not allowed ")
except ValueError:
    print(f"Invalid input")
else:  # if not then it will run 
    print(f"ans = {ans}")

    # for other built in exception visit w3 school
