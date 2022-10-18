def interpolationSearch(arr: list, element: int) -> int:
    low = 0
    high = (len(arr) -1)
    while low <= high and element >= arr[low] and element <= arr[high]:
        index = low + int(((float(high - low) / ( arr[high] - arr[low])) * ( element - arr[low])))
        if arr[index] == element:
            return index
        if arr[index] < element:
            low = index + 1;
        else:
            high = index - 1;
    return -1

lists = [1,2,3,4,5,6,7,8]
print(interpolationSearch(lists, 6))
