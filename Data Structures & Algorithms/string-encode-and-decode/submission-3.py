class Solution:

    def encode(self, strs: List[str]) -> str:
        # time: O(L）L is the total length in all strings
        # space: O(1)
        res = ""
        for st in strs:
            res += str(len(st)) + "#" + st
        
        return res

    def decode(self, s: str) -> List[str]:
        # time: O(n), where n is the length of s
        # space: O(n) becasue of res
        res = []
        i = 0
        while i < len(s):
            j = i

            # find the hash symbol
            while s[j] != '#':
                j += 1
            
            length = int(s[i:j])
            res.append(s[j+1: j + 1 + length])
            i = j + 1 + length
        
        return res
