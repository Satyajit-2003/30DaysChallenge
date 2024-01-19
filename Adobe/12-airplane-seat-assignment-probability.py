# Pure Maths Question, we can proof that f(n) = 0.5, for n >= 2 using mathematical induction

class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        if n == 1:
            return 1.0
        return 0.5