#Given an unsorted array of size N, rotate it by D elements (clockwise).

A=list(eval(input("Enter Array : ")))
N=len(A)

D=int(input("Enter Number of Elements to be rotated in Clockwise Direction : "))

for i in range(D):
    A.insert(0,A[-1])
    A.pop()

print(A)
