# Code to illustrate complex number

# covert real number to complex
num = complex(5,3)
print(num)

# covert real number to complex
num = complex(5,-4)
print(num)

# Default if no parameter is passed to complex method
num = complex()
print(num)

# In case if you pass only real number, defaults imaginary to 0
num = complex(5)
print(num)

# In case if you pass only real number, defaults imaginary to 0
num = complex(-2)
print(num)

# In case if you pass only float number, defaults imaginary to 0
num = complex(5.6,4)
print(num)

# if string is passed, it will be interpreted as complex number
num = complex('8')
print(num)

# if string is passed, it will be interpreted as complex number
num = complex('1+2j')
print(num)
