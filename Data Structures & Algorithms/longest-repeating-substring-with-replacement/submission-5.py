class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        n = len(s)
        

        res = 0
        for c in charSet:
            count = 0
            left = 0
            # extend the slide window
            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                
                # invalid widnow 
                while (right - left + 1) - count > k:
                    if s[left] == c:
                        count-= 1
                    left += 1
                
                res = max(res, right - left + 1)
        
        return res
