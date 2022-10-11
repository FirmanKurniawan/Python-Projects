from math import log
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from prettytable import PrettyTable
from scipy.interpolate import make_interp_spline

Literacy_Population = [61, 55, 45, 88, 99, 55, 12, 67, 22, 56, 55, 14, 12, 99, 2, 12, 8, 6, 11, 9, 19, 21, 26, 14, 16,
                       77, 79, 11, 48, 28, 30, 45, 89, 44, 91, 55, 33, 90, 33, 55, 71, 50, 91, 23, 21, 20, 17, 19, 7, 1,
                       79, 22, 11, 77, 98, 62, 16, 14, 43, 22, 2, 8, 68, 37, 28, 32, 53, 90, 36, 80, 42, 56, 40, 43, 36,
                       53, 45, 65, 24, 24, 47, 57, 57, 19, 17, 34, 35, 27, 63, 73, 24, 84, 67, 45, 56, 5, 44, 34,
                       89, 18, 13, 9]

Literacy_Population.sort()
print("Sorted list : ", Literacy_Population)
N = len(Literacy_Population)
l = log(N, (10))

k = 1 + 3.22 * l
print("Number of Classes : ", k)

h = (max(Literacy_Population) - min(Literacy_Population)) / 7
print("Width of class : ", h)

print("Minimum Value is : ", min(Literacy_Population))
print("Maximum Value is : ", max(Literacy_Population))
print("Classes in this data are : ")
m = min(Literacy_Population)

for c in range(0, 7):
    d = m + 13
    print(m, "--", d)
    m = d + 1

f1 = 0
for a in Literacy_Population:
    if a >= 1 and a <= 14:
        f1 = f1 + 1
print("Values in range 1--10 are : ", f1)

f2 = 0
for a in Literacy_Population:
    if a >= 15 and a <= 28:
        f2 = f2 + 1
print("Values in range 15--28 are : ", f2)

f3 = 0
for a in Literacy_Population:
    if a >= 29 and a <= 42:
        f3 = f3 + 1
print("Values in range 29--42 are : ", f3)

f4 = 0
for a in Literacy_Population:
    if a >= 53 and a <= 56:
        f4 = f4 + 1
print("Values in range 53--56 are = ", f4)

f5 = 0
for a in Literacy_Population:
    if a >= 57 and a <= 70:
        f5 = f5 + 1
print("Values in range 57--70 are = ", f5)

f6 = 0
for a in Literacy_Population:
    if a >= 71 and a <= 84:
        f6 = f6 + 1
print("Values in range 71--84 are = ", f6)

f7 = 0
for a in Literacy_Population:
    if a >= 85 and a <= 99:
        f7 = f7 + 1
print("Values in range 85--99 are = ", f7)

c_f1 = f1
print("\nCommulative Frequency of class 1 is : ", c_f1)
c_f2 = c_f1 + f2
print("Commulative Frequency of class 2 is : ", c_f2)
c_f3 = c_f2 + f3
print("Commulative Frequency of class 3 is : ", c_f3)
c_f4 = c_f3 + f4
print("Commulative Frequency of class 4 is : ", c_f4)
c_f5 = c_f4 + f5
print("Commulative Frequency of class 5 is : ", c_f5)
c_f6 = c_f5 + f6
print("Commulative Frequency of class 6 is : ", c_f6)
c_f7 = c_f6 + f7
print("Commulative Frequency of class 7 is : ", c_f7)

r_f1 = f1 / N
print("\nRelativive frequency of Class 1 : ", r_f1)
r_f2 = f2 / N
print("Relativive frequency of Class 2 : ", r_f2)
r_f3 = f3 / N
print("Relativive frequency of Class 3 : ", r_f3)
r_f4 = f4 / N
print("Relativive frequency of Class 4 : ", r_f4)
r_f5 = f5 / N
print("Relativive frequency of Class 5 : ", r_f5)
r_f6 = f6 / N
print("Relativive frequency of Class 6 : ", r_f6)
r_f7 = f7 / N
print("Relativive frequency of Class 7 : ", r_f7)
t1 = r_f1 + r_f2 + r_f3 + r_f4 + r_f5 + r_f6 + r_f7
print("Total Relative Frequency = ", t1)

p_f1 = r_f1 * 100
print("\nPercentage Frequency of Class 1 : ", p_f1)
p_f2 = r_f2 * 100
print("Percentage Frequency of Class 2 : ", p_f2)
p_f3 = r_f3 * 100
print("Percentage Frequency of Class 3 : ", p_f3)
p_f4 = r_f4 * 100
print("Percentage Frequency of Class 4 : ", p_f4)
p_f5 = r_f5 * 100
print("Percentage Frequency of Class 5 : ", p_f5)
p_f6 = r_f6 * 100
print("Percentage Frequency of Class 6 : ", p_f6)
p_f7 = r_f7 * 100
print("Percentage Frequency of Class 7 : ", p_f7)
t2 = p_f1 + p_f2 + p_f3 + p_f4 + p_f5 + p_f6 + p_f7
print("Total Percentage Frequency = ", t2)
frequency = [f1, f2, f3, f4, f5, f6, f7]
print("\n Table ")
myTable = PrettyTable(["Classes", "Frequency", "C_F", "R_F", "%_F", "C_B"])
myTable.add_row(["1--10", f1, c_f1, r_f1, p_f1, "0.5--10.5"])
myTable.add_row(["15--28", f2, c_f2, r_f2, p_f2, "14.5--29.5"])
myTable.add_row(["29--42", f3, c_f3, r_f3, p_f3, "28.5--42.5"])
myTable.add_row(["53--56", f4, c_f4, r_f4, p_f4, "52.5--56.5"])
myTable.add_row(["57--70", f5, c_f5, r_f5, p_f5, "56.5--70.5"])
myTable.add_row(["71--84", f6, c_f6, r_f6, p_f6, "50.5--84.5"])
myTable.add_row(["85--99", f7, c_f7, r_f7, p_f7, "84.5--99.5"])
print(myTable)

classes_list = [0.5, 10.5, 29.5, 42.5, 56.5, 70.5, 84.5, 99.5]
sns.set()
plt.hist(Literacy_Population, bins=classes_list)
plt.xlabel("CB")
plt.ylabel("Frequency")
plt.legend(["Literacy Population", "Frequency"])
plt.title("HISTORAM")
plt.show()

p = np.array([0.5, 10.5, 29.5, 42.5, 56.5, 70.5, 84.5, 99.5])
q = np.array([20, 22, 12, 10, 9, 8, 10, 0])
X_Y_Spline = make_interp_spline(p, q)
X_ = np.linspace(p.min(), p.max(), 500)
Y_ = X_Y_Spline(X_)
plt.xlabel("CB")
plt.ylabel("Frequency")
plt.legend(["Literacy Population", "Frequency"])
plt.title("FREQUENCY CURVE")
plt.plot(X_, Y_)
plt.show()

intervals = [0.5, 10.5, 29.5, 42.5, 56.5, 70.5, 84.5, 99.5]
plt.xticks(intervals)
frequency, edges, _ = plt.hist(Literacy_Population, histtype='step', bins=intervals)
midpoints = 0.5 * (edges[1:] + edges[:-1])
plt.plot(midpoints, frequency, 'go--')
plt.title("FREQUENCY POLYGON")
plt.xlabel("CB")
plt.ylabel("FD")
plt.show()

mylables = ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7"]
plt.pie(frequency)
plt.legend(mylables)
plt.title("PIE CHART")
plt.show()

Provinces = ["ISLAMABAD", "PUNJAB", "G_B", "KPK", "BALOCH", "SINDH", "AJK"]
Literacy = [345, 520, 365, 397, 410, 415, 537]

sns.barplot(x=Provinces, y=Literacy)
plt.title("Literacy Population Data 10 Years and Older")
plt.show()

plt.pie(Literacy)
plt.legend(Provinces)
plt.title("Literacy Population Data 10 Years and Older")
plt.show()
