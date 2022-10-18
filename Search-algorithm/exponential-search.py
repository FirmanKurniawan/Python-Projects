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


def exponentialSearch(arr: list, element: int) -> int:
    if arr[0] == element:
        return 0
    index = 1
    while index < len(arr) and arr[index] <= element:
        index = index * 2
    return binarySearch(arr[:min(index, len(arr))], element)

lists = [1,2,3,4,5,6,7,8,9]
print(exponentialSearch(lists, 3))
