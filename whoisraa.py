x = 9
def diamond_pattern():
    print("Diamond Pattern")
    for i in range(1, (x+1)//2 + 1): 
        for j in range((x+1)//2 - i):
            print(" ", end = "")
        for k in range((i*2)-1):
            print("*", end = "")
        print()

    for i in range((x+1)//2 + 1, x + 1): 
        for j in range(i - (x+1)//2):
            print(" ", end = "")
        for k in range((x+1 - i)*2 - 1):
            print("*", end = "")
        print()
        
diamond_pattern()
