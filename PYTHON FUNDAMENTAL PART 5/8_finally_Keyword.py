# finally keyword 
try:
    x=int(input("Enter x : "))
    ans = 10/x 

except ZeroDivisionError: # if exception throws then it run 
    print("Divide by 0 is not allowed ")

except ValueError:
    print(f"Invalid input")

else:  # if not then it will run 
    print(f"ans = {ans}")
finally: # it will run irrespective of error thrown or not 
    print("End of program")