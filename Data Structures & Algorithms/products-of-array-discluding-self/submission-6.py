class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * (len(nums)+1)
        suffix = [0] * (len(nums)+1)
        prefix[0] = 1
        suffix[len(nums)-1] = 1

        prod = 1
        for i, val in enumerate(nums):
            prefix[i] = prod
            prod *= val


        prod = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]

        res = [0] * len(nums)
        
        for i in range(len(nums)):
            # print (prefix, suffix)
            res[i] = prefix[i] * suffix[i]
        return res