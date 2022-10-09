# Python program for implementation of MergeSort

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1) # First sub array from arr[l...m]
    R = [0] * (n2) # second sub array frim arr[m+1...r]

    # Copy elements to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0    # Initial index of first subarray
    j = 0    # Initial index of second subarray
    k = l    # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergeSort(arr, l, r):
    if l < r:
        m = (l + r)//2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


# Driver code
lis=[2,8,3,2,9,8,6,5,3,1,9,0,0,0,6,7,9,5,5,4,3,2,1,7,8]
n = len(lis)
print("Given array is")
print(*lis)

mergeSort(lis,0,n-1)
print("\n\nSorted array is")
print(*lis)