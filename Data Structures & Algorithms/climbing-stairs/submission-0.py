class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 2: return 2
        a, b = 0,1
        for i in range(1, n+1):
            a , b = b, a+ b
        return b
        