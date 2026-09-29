class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 同字母乱序
        
        if (len(s) != len(t)):
            return False
        
        s_hashMap = {}
        t_hashMap = {}
        for i in range(len(s)):
            if s[i] not in s_hashMap:
                s_hashMap[s[i]] = 1
            else:
                s_hashMap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in t_hashMap:
                t_hashMap[t[i]] = 1
            else:
                t_hashMap[t[i]] += 1

        return s_hashMap == t_hashMap