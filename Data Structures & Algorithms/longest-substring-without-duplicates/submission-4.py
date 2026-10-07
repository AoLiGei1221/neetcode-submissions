class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        n = len(s)
        ans = 0
        left = 0

        for right, ch in enumerate(s):
            # check if in my sliding window
            while ch in char_set:
                #move the left pointer and left character
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])

            ans = max(right - left + 1, ans)
        
        return ans