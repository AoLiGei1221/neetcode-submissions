class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # sorting
        # Time: O(N * logN)
        # space: O(1) or O(N) depending on the algo
        nums.sort()
        for i in range(0, len(nums) - 1):
            # find duplicates
            if nums[i] == nums[i+1]:
                return True
        
        return False