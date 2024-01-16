class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # we can have as many z as we want in the substring. 
        # These combinations can't be there: xx, yy, xz, zy

        # When the x == y we can use all the substrings
        # Use x and y alternatively, append z at the end or beginning
        if x == y:
            return 2 * (2*x + z)
            
        # When x != y we can start with the x or y whichever is higher, and go alternatively
        # If it starts with x, append z in the beginning, else append z in the end
        return 2 * (2*min(x, y) + z + 1)
        