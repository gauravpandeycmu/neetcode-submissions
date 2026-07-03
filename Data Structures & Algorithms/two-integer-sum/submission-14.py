class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, val in enumerate(nums):
            A.append([val, i])
        A.sort()

        i, j = 0, len(A)-1

        while i<j:
            val1 = A[i][0]
            val2 = A[j][0]

            if val1+val2 == target:
                return [min(A[i][1], A[j][1]), max(A[i][1], A[j][1])]
            elif val1+val2 > target:
                j -= 1
            else:
                i += 1
        return []