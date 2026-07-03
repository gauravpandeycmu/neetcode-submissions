class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1

        while l<r:
            ele1 = numbers[l]
            ele2 = numbers[r]

            if ele1+ele2 == target:
                return [l+1, r+1]
            elif ele1+ele2 < target:
                l += 1
            else:
                r -= 1
            

        