import numpy as np
import matplotlib.pyplot as plt


def collatz(n):
    global yvalues, xvalues
    yvalues = []
    xvalues = []
    count = 0
    while n > 1:
        xvalues.append(count)
        count += 1
        yvalues.append(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n = n // 2
    print(yvalues, '\n', "Iterations = ", count, '\n')


def result():
    for i in range(1, 100001):
        print("Sequence = ", end="")
        collatz(i)
        plt.plot(np.array(xvalues),
                 np.array(yvalues),
                 color='black',
                 marker='o',
                 markerfacecolor='yellow',
                 markersize=3)
        try:
            mvalues = np.max(np.array(yvalues))
            plt.annotate(mvalues,
                         (np.array(yvalues).argmax(), mvalues),
                         textcoords="offset points",
                         xytext=(0, 5),
                         ha='center')
        except ValueError:
            pass


plt.title("Collatz")
plt.xlabel("Iterations/Steps")
plt.ylabel("Numbers")
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
result()
plt.grid()
plt.show()
