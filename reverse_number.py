# Program to reverse the digits of a number 

def reverse(n):
    rev = 0
    while(n):
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev

if __name__ == '__main__':
    n = 10203040506070809
    rev = reverse(n)
    print(f"Reverse of {n} is {rev}")