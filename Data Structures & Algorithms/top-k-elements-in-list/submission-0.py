class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for i in nums:
            res[i] = 1 + res.get(i, 0)
        
        arr = []
        for num, cnt in res.items():
            arr.append([cnt, num])
        arr.sort()

        ans = []
        while len(ans) < k:
            ans.append(arr.pop()[1])
        
        return ans

        

        