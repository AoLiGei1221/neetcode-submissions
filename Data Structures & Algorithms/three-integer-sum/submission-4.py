class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # time: O(n^2)
        # space: O(1)
        # Note that the answer should not contain any duplicate triplets
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n-2):
            a = nums[i]

            # single number is too big since we already sory the array
            if a > 0:
                break
            
            # first three numbers > 0, other numbers must also > 0 since sort
            if a + nums[i+1]+ nums[i+2] > 0:
                break

            # add with two largest number but cannot reach 0, then add other must cannot reach 0
            if a + nums[-1] + nums[-2] < 0:
                continue
            
            # skip the repeat numbers bc same tuple is not allowed
            if i > 0 and a == nums[i-1]:
                continue

            left = i + 1
            right = n - 1
            while left < right:
                b = nums[left]
                c = nums[right]
                three_sum = a + b + c

                if three_sum == 0:
                    res.append([a, b, c])
                    left += 1
                    right -= 1
                    # skip the repeated numbers
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
            

