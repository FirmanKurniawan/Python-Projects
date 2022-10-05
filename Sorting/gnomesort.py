def gnomeSort(a:list)->list:
    pos:int = 0
    while pos < len(a):
        if (pos == 0 or a[pos] >= a[pos-1]):
            pos += 1
        else:
            a[pos],a[pos-1] = a[pos-1],a[pos]
            pos -= 1

number:list = [6,5,3,1,8,7,2,4]
gnomeSort(number)
print(number)