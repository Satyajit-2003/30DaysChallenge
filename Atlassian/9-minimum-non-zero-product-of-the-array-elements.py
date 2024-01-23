# Explanation:

# Our aim is to get as many 1 as possible, so that product is minimized
# Let's take an example: p = 4
# Assuming p = 4:
# 0001
# 0010
# 0011
# 0100
# 0101
# 0110
# 0111
# 1000
# 1001
# 1010
# 1011
# 1100
# 1101
# 1110
# 1111

# In the right most column all 1's float up to the top. In the other columns the 1's float down and you would get the below result :

# 0001
# 0001
# 0001
# 0001
# 0001
# 0001
# 0001
# 1111
# 1110
# 1110
# 1110
# 1110
# 1110
# 1110
# 1110


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 1000000007
        n = pow(2, p) - 1
        return (n * pow(n - 1, n//2, MOD)) % MOD