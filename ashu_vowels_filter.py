a=list(input().lower())
b=["a", "o", "y", "e", "u", "i"]
c=[]
for i in a:
    if i not in b:
        c.append(i)
for i in range(2*len(c)):
    if i%2==0:
        c.insert(i,".")
a=""
for i in c:
    a+=i
print(a)
