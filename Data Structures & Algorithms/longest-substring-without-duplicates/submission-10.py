class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        n = len(s)
        ans = 0

        for right, ch in enumerate(s):
            while ch in char_set:
                char_set.remove(s[left])
                left += 1

            # add it into the char_set
            char_set.add(s[right])

            ans = max(ans, right - left + 1)
        
        return ans
        

        