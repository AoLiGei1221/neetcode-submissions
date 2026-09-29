class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sorting
        nums.sort()
        for i in range(0, len(nums) - 1):
            # find duplicates
            if nums[i] == nums[i+1]:
                return True
        
        return False