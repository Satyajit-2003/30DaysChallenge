# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# Find the peak using binary search. 
# Then do binary search on the left and right side of the peak.
# If not found, return -1.


class Solution:
    def findInMountainArray(self, target: int, moun_arr: 'MountainArray') -> int:
        l, r = 1, moun_arr.length()-2
        while l <= r:
            mid = (l + r)//2
            prev, next, m = moun_arr.get(mid-1), moun_arr.get(mid+1), moun_arr.get(mid)
            if prev < m < next:
                l = mid + 1
            elif prev > m > next:
                r = mid - 1
            else:
                break
        
        peak = mid

        l, r = 0, peak

        while l <= r:
            mid = (l + r) // 2
            val = moun_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        l, r = peak, moun_arr.length() - 1

        while l <= r:
            mid = (l + r) // 2
            val = moun_arr.get(mid)
            if val == target:
                return mid
            elif val < target:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
