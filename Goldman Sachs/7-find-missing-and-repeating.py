# Maths formulae
# sum = n(n+1)/2
# sum of sq = n(n+1)(2n+1)/6

# x-> missing
# y-> repeat

# x+y = sum-sum(arr)
# x^2-y^2 = sum of sq - sum_of_sq(arr)

# find  x and y 


class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        su = su2 = 0
        for num in arr:
            su += num
            su2 += (num**2)
        diff = ((n*(n+1))/2)- su
        prod = ((n*(n+1)*(2*n+1))/6) - su2
        sum_ = prod / diff
        
        miss = (diff+sum_) / 2
        rep = sum_- miss
        
        return [int(rep), int(miss)]