def mergeSort(n,lis):
    if n<2:
        print(lis)
        return n
    else:
        mergeSort((n // 2), lis)
        print(lis)
        bubleSort(n,lis)
        print(lis)

def bubleSort(n,lis):
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if lis[j] > lis[j + 1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

lis=[2,8,3,2,9,8,6,5,3,1,9,0,0,0,6,7,9,5,5,4,3,2,1,7,8]
mergeSort(len(lis),lis)
