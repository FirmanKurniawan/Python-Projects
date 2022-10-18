

def binarySearch(arr: list, element: int) -> int:
    first = 0
    last = len(arr)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if arr[mid] == element:
            index = mid        
        else:
            if element <arr[mid]:
                last = mid -1

            else:
                first = mid +1

    return index

lists = [10,20,30,40,50]
print(binarySearch(lists, 20))
