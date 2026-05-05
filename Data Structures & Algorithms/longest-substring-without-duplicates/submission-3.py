class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        ans = [0] * n
        ans[0] = 1

        last_seen = {s[0]: 0}
        for i in range(1, n):
            if s[i] not in last_seen:
                ans[i] = ans[i-1] + 1
            else:
                distance = i - last_seen[s[i]]
                ans[i] = min(ans[i-1] + 1, distance)

            last_seen[s[i]] = i # 更新位置
        
        
        return max(ans)
        