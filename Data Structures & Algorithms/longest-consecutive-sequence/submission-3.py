class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in nums:
            # optimization
            # 如果前一个数还在的话 那就不可能是起点了 =》也就是说不需要检查了
            if num - 1 not in store:
                # streak record the longest sequence
                # curr is the current looping number
                # think curr is the starting number
                streak, curr = 0, num
                while curr in store:
                    streak += 1
                    curr += 1
                res = max(streak, res)
            
        return res
        