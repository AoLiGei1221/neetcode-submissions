class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # time: O(N)
        # Space: O(N)
        hashMap = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hashMap:
                hashMap[num] = 1
            else:
                hashMap[num] += 1

        for key, value in hashMap.items():
            # we have duplicates
            if value > 1:
                return True
        
        return False
        