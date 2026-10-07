class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # dp[i] = the length of the longest substring without repeating characters ENDING at index i
        # dp[i] = dp[i-1] + 1, if no repeating
        # i - last_seen[s[i]] : distance between current and previous occurrence
        # dp[i] = min(dp[i-1] + 1, i - last_seen[s[i]])

        if not s:
            return 0
        n = len(s)
        dp = [0] * n
        dp[0] = 1
        # record the last time we see in the index
        last_seen = {s[0] : 0} 

        for i in range(1, n):
            # for sure we will add it into the sequence
            if  s[i] not in last_seen:
                dp[i] = dp[i-1] + 1
            else:
                # since repeating, now the longest safe string
                distance = i - last_seen[s[i]]
                dp[i] = min(distance, dp[i-1] + 1)
            
            last_seen[s[i]] = i
        
        return max(dp)
        