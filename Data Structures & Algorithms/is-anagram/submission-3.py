class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 同字母乱序
        
        if (len(s) != len(t)):
            return False
        
        s_hashMap = {}
        t_hashMap = {}
        for i in range(len(s)):            
            s_hashMap[s[i]] = 1 + s_hashMap.get(s[i], 0)
            t_hashMap[t[i]] = 1 + t_hashMap.get(t[i], 0)
        return s_hashMap == t_hashMap