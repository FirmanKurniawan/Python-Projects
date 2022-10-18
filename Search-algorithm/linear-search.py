def linearSearch(arr: list, element: int) -> int:
    for i in range (len(arr)) :
        if arr[i] == element:
            return i
    return -1

lists = [1,2,3,4,5,6,7,8,9]
print(linearSearch(lists, 3))
