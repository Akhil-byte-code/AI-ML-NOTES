# Q1. Write a program that asks the user for their name and age, then prints a
# sentence like:

# name = input("enter your name :")
# age = int(input("Enter your age :"))

# print("Hello", name, "you are" , age, "years old ")


# Q2. Take two numbers as input from the user and print their sum, difference,
# product, and quotient.

# a = int(input("Enter first num "))
# b = int(input("Enter second num "))

# print("Sum" , a+b )
# print("Diffeence" , a-b)
# print("Product", a*b)
# print("Quotient" , a//b)


# Q3. Ask the user to enter two integers and one float. Convert them all to floats
# and print their average.

# a = int(input("Enter first num "))
# b = float(input("Enter second num "))
# a = float(a)

# avg = (a + b)/2
# print("Avg of two number " , avg)



# Q4. The user enters a string containing a number (e.g., "45" ). Convert it to:
# • an integer
# • a float
# • a string again
# Print all three values with their types.

# stri  = "45"
# intVal = int(stri)
# print(intVal)
# floatval = float(stri)
# print(floatval)
# stringAgain = str(floatval)
# print(stringAgain)


# Q5. Evaluate and print the result of the following expression:
# x = 10 + 3 * 2 ** 2
# Based on what you learnt in the lecture explain why the output is what it is.
# print(x)

# Q6. Write a program to swap values of two numbers entered by the user.
# a = 10 
# b = 5 
# print( a, b)
# new = a 
# a = b 
# b = new
# print( a, b)


# Q7. Ask the user for a temperature in Celsius (string input). Convert it to float ,
# then calculate and print temperature in Fahrenheit.
# Conversion formula: F ahrenheitT emp = (CelsiusT emp ∗ (9/5)) + 32

# temp = input("Enter the temp ")
# tempnew = float(temp)
# FahrenheitTemp = (tempnew * (9/5)) + 32
# print(FahrenheitTemp)
                  

# Q8. Take the radius (r) as user input and print the area.
# Use the formula: Area = π * r2 (value of π = 3.14)
radius = int(input("Enter the result "))
area = 3.14*(radius**2)
print("Area of circle " , area)