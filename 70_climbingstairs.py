# Original answer worked but exceeded time, had to review other answers
# Can't take credit for this one, again it is more about knowledge of mathematical concepts.  Now I know both
# A method of calculating square roots and how to essentially do a new flavor of series summation
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    S = Solution()
    args = [45]
    for arg in args:
        print(S.climbStairs(arg))