class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n-1

        while left<right:
            mid = left + (right-left)//2

            if nums[mid] < nums[right]:
                right = mid 
            else:
                left = mid + 1
        pivot = left

        def bs(left, right):
            while left<=right:
                mid = left + (right-left)//2
                if nums[mid] == target:
                    return mid
                elif nums[mid]<target:
                    left = mid +1
                else:
                    right = mid-1
            return -1
        
        res = bs(0, pivot) 
        if res!= -1:
            return res
        return bs(pivot, n-1)