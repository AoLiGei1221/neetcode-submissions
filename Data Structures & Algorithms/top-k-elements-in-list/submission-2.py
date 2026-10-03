class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # time: O(nlogn)
        # space: O(n)
        freq = {}
        res = []

        # build the hash map
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
        keys_list = list(freq.keys())
        for i in range(k):
            res.append(keys_list[i])
        
        return res
        