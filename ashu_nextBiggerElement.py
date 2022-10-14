def nextBiggerElement(arr):
    stack=[]
    res=[]
    for i in range(len(arr)-1,-1,-1):
        
        while len(stack)!=0 and stack[-1]<=arr[i]:
            stack.pop()
        
        if len(stack)==0:
            res.insert(0,-1)
        else:
            res.insert(0,stack[-1])
        stack.append(arr[i])
    print(*res)   
array=[3,10,5,1,15,10,7,6]
nextBiggerElement(array)
