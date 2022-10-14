# Define the function to calculate power
def cal_power(n):    
    return x ** n

# Take the value of x
x = int(input("Enter the value of x:"))
# Define a tuple of numbers
numbers = [2, 3, 4]

# Calculate the x to the power n using map()
result = map(cal_power, numbers)
print(list(result))
