class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        longest = 0

        for i in range(len(nums)):
            curr_num = nums[i]
            tmp = 1

            while (curr_num + 1) in nums:
                curr_num += 1
                tmp += 1

            longest = max(tmp, longest)

        return longest