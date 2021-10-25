import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(threshold=1000000)


def prime_numbers(n):
    global list_of_primes
    list_of_primes = []
    for num in range(2, n+1):
        if all(num % i != 0 for i in range(2, num)):
            list_of_primes.append(num)


def function_on_primes():
    global list_of_ret_func
    list_of_ret_func = []
    for x in list_of_primes:
        ga = bin(x).replace("0b", "")
        gb = str(ga)[::-1]
        list_of_ret_func.append(int(str(gb), 2))
    list_of_ret_func = list(map(int, list_of_ret_func))


def subtract_arrays():
    g = np.subtract(np.array(list_of_primes), np.array(list_of_ret_func))
    plt.scatter(np.array(list_of_primes), g, s=1)


n = int(input("enter number- "))
prime_numbers(n)
function_on_primes()
subtract_arrays()

plt.title("Prime Parallelograms")
plt.xlabel("f(p(n)")
plt.ylabel("Prime Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.show()
