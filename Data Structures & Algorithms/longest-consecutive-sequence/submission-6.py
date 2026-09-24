class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0

        for i in nums:
            temp = 0
            if i-1 in s:
                continue

            num = i
            while num in s:
                temp += 1
                num+=1
            res = max(res, temp)
            
        return res