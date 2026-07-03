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
            elif cur < target:
                l += 1
            else:
                r -= 1
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i, ele in enumerate(nums):
            temp = self.twoSum(nums, i+1, len(nums)-1, -ele)

            for j in temp:
                res.add( (ele, nums[j[0]], nums[j[1]]) )
        return [x for x in res]