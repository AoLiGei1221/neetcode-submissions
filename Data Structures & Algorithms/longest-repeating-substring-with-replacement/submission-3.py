class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        l = 0
        res = 0

        # 看每一个char可以最多多少
        for c in charSet:
            count_mismatch = 0
            l = 0
            # extend the right 
            for r in range(len(s)):
                # acculerate the number of mismatch
                if s[r] != c:
                    count_mismatch += 1
                
                # window is invalid 
                while count_mismatch > k:
                    # keep shrinking the window and check the char
                    # if not equal to what we want char, then we decrease mismatch by 
                    # one since we gonna move the left pointer
                    if s[l] != c:
                        count_mismatch -= 1
                    l += 1
                
                res = max(res, r - l + 1)
        
        return res



        

                
