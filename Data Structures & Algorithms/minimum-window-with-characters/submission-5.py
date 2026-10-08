class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # sliding windpw
        if t == "":
            return ""
        
        res = ""
        resLen = float('inf')
        # need
        countT ={}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        countS = {}
        have = 0
        need = len(countT)

        res = ""
        resLen = float('inf')

        left = 0
        for right in range(len(s)):
            c = s[right]

            countS[c] = 1 + countS.get(c, 0)

            if c in countT and countT[c] == countS[c]:
                have += 1
            
            # shrink the window
            while have >= need:
                # get current length
                curr_len = right - left + 1
                if curr_len < resLen:
                    resLen = curr_len
                    res = s[left:right+1]
            
                # remove the char in left idx
                countS[s[left]] -= 1

                if s[left] in countT and countT[s[left]] > countS[s[left]]:
                    have -= 1 

                left += 1
        
        return res