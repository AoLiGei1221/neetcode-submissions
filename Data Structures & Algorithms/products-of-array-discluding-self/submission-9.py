class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix product: [1, 2, 6, 24]
        # postfix product: [24, 24, 12, 4]

        postfix = []
        prefix = [1] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            prefix[i] = prod
        prod = 1
        for i in range(len(nums) - 1, -1, -1):  # 正确的逆序遍历
            prod *= nums[i]
            postfix.append(prod)
            
        postfix.reverse()  # 必须反转，否则后缀乘积顺序是反的

        res = [1] * len(nums)
        for i in range(len(nums)):
            # normal case
            if i - 1 >= 0 and i+1 <= len(nums) - 1:
                res[i] = prefix[i-1] * postfix[i+1]
            # left side exceed then we only take the right part, exclude the curr index
            elif i - 1 < 0:
                res[i] = postfix[i+1]
            # right side exceed then we only take the left part, exclude the curr index
            elif i + 1>len(nums) - 1:
                res[i] = prefix [i - 1]

        return res
        


        