class Solution:
    def sumScores(self, s: str) -> int:
        z_arr = [0 for i in range(len(s))]
        l, r = 0,0
        n = len(s)
        for i in range(1,len(s)):
            if i > r:
                l, r = i, i
                while r < n and s[r-l]==s[r]:
                    r += 1
                z_arr[i] = r-l
                r -= 1
            else:
                k = i - l
                if z_arr[k] < (r-i+1):
                    z_arr[i] = z_arr[k]
                else:
                    l = i 
                    while r < n and s[r-l] == s[r]:
                        r += 1
                    z_arr[i] = r - l
                    r -= 1
        return sum(z_arr) + len(s)
