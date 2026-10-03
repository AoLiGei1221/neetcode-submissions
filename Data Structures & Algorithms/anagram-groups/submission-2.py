class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            sorted_str = ''.join(sorted(st))
            if sorted_str in res:
                res[sorted_str].append(st)
            else:
                res[sorted_str] = [st]
        
        return list(res.values())


        