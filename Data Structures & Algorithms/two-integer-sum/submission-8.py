class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}

        for i, val in enumerate(nums):
            j = target - val

            if j in m:
                return [m.get(j), i]

            m[val] = i

