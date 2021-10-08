# 0-1 Knapsack Problem
# Returns the maximum value that can be put in a knapsack of capacity W
 
def knapSack(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
 
    # If weight of the nth item more than Knapsack of capacity then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)
    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))
# end of function knapSack
 
#Main Code
val = [70, 150, 200]   #values 
wt = [10, 20, 30]   #weights
W = 50  #capacity=50
n = len(val)    #number of objects to choose form
print (knapSack(W, wt, val, n)) 