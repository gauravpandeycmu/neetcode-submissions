class Solution:
    def twoSum(self, nums, start, end, target):
        l, r = start, end
        res = []

        while l<r:
            cur = nums[l] + nums[r]

            if cur == target:
                res.append([l, r])
                l += 1
                r -= 1

                while l<r and nums[l] == nums[l-1]:
                    l += 1
                while l<r and nums[r] == nums[r+1]:
                    r -= 1
            elif cur < target:
                l += 1
            else:
                r -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, ele in enumerate(nums):
            if i>0 and nums[i] == nums[i-1]:
                continue

            for l, r in self.twoSum(nums, i+1, len(nums)-1, -ele):
                res.append( [ele, nums[l], nums[r]] )
        return res