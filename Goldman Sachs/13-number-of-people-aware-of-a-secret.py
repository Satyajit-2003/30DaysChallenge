# Use DP to store how many people know the secret on each day
# At each day, we add the number of people who know the secret on that day
# and subtract the number of people who forgot the secret on that day
# End result is the sum of the last forget days

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0 for _ in range(n+1)]
        dp[1] = 1 # 1 person knows on 1st day
        sharing = 0

        for i in range(2, n+1):
            new = dp[max(i-delay, 0)]
            forgot = dp[max(i-forget, 0)]
            sharing += (new - forgot)

            dp[i] = sharing
        
        return sum(dp[-forget:]) % MOD