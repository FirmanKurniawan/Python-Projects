# Quicksort algorithm by taking last element as pivot

def partitionIndex(arr, l, r):
    i = l - 1
    pivot = arr[r]

    for j in range(l, r):
        if arr[j] <= pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[r] = arr[r], arr[i+1]
    return (i+1)

def quicksort(arr, l, r):
    if l < r:
        index = partitionIndex(arr, l ,r)
        quicksort(arr, l, index-1)
        quicksort(arr, index+1, r)

if __name__ == '__main__':
    arr = [106, 503, 444, 22, 90, 34, 108, 34, 73, 88, 66, 444, 10, 90]
    n = len(arr)
    quicksort(arr, 0, n-1)
    print(arr)