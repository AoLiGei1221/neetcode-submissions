class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            a = nums[i]

            # too big
            if a > 0:
                break
            
            # remove the repeat numbers
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
                    # 去掉重复的
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif three_sum > 0:
                    right -= 1
                else:
                    left += 1
        
        return res
            

