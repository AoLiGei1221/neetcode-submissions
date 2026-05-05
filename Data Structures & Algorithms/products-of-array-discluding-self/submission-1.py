class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod, zero_count = 1, 0
        for num in nums:
            # get non-zero product
            if num != 0:
                prod *= num
            else:
                zero_count += 1
        # exist two zeros means 0's array
        if zero_count > 1: return [0] * n

        res = [0] * n
        for i in range(n):
            if zero_count:
                res[i] = prod if nums[i] == 0 else 0
            else:
                res[i] = prod // nums[i]
        
        return res