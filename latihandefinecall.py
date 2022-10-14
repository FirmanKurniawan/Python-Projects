# Define addition function
def addition(number1, number2):
    result = number1 + number2
    print("Addition result:",result)

# Define area function with return statement
def area(radius):
    result = 3.14 * radius * radius
    return result  

# Call addition function
addition(400, 300)
# Call area function
print("Area of the circle is",area(4))
