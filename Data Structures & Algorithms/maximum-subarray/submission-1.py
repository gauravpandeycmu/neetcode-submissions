class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        right = 0
        n = len(nums)
        res = max(nums)

        while right<n:
            cur = 0

            while right<n and cur + nums[right] > 0:
                cur += nums[right]
                right += 1

                res = max(res, cur)
            right += 1
        return res
            