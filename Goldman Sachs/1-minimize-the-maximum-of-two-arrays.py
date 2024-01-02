# Use binary search betwn 1-10^10
class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, cnt1: int, cnt2: int) -> int:
        def lcm(d1, d2):
            # Find GCD first
            x, y = d1, d2
            while d2:
                d1, d2 = d2, d1 % d2

            return (x * y) // d1

        def satisfy(d1, d2, c1, c2, mid):
            notDivByd1 = mid - (mid // d1)
            notDivByd2 = mid - (mid // d2)
            notDivByBoth = mid - (mid // lcm(d1, d2))

            if (
                notDivByd1 >= c1
                and notDivByd2 >= c2
                and notDivByBoth >= c1 + c2
            ):
                return True
            return False

        res = 10**10
        l, r = 2, 10**10
        while l <= r:
            mid = l + ((r - l) // 2)
            if satisfy(divisor1, divisor2, cnt1, cnt2, mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
