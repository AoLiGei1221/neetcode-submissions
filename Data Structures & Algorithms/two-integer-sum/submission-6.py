class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        A = []
        for i, num in enumerate(nums):
            A.append([num, i])
        
        A = sorted(A, key=lambda x: x[0])
        left, right = 0, len(nums) - 1
        while (left < right):
            if A[left][0] + A[right][0] > target:
                right -= 1
            elif A[left][0] + A[right][0] < target:
                left += 1
            else:
                return sorted([A[left][1], A[right][1]])