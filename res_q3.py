# Write a program in Python to demonstrate the use of try, except, else, and finally
# blocks in exception handling.

# Implement a function that takes two numbers as input and attempts to divide them.

# Use the try block to perform the division operation,

# the except block to handle division by zero and invalid input errors,

# the else block to print the result if no exception occurs,

# and the finally block to display a message indicating the end of execution.

class Div:
    
    def divide(self, num1, num2):
        try:
            result = num1/num2
        except ZeroDivisionError as zde:
            print(f"Exception occurred: {str(zde)}") 
        else:
            print(f"Result: {result}") 
        finally:
            print("Program execution complete.")
            
d1 = Div()

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

d1.divide(num1, num2)