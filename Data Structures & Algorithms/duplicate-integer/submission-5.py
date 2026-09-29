class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Hash Set method
        # O(N)
        # O(N)

        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        
        return False
