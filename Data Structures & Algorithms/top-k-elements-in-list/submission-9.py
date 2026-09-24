class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for i in nums:
            freq[i] += 1

        arr = []

        for i, j in freq.items():
            arr.append([j, i])

        arr.sort()

        res = []

        for i in range(k):
            res.append(arr[len(arr)-i-1][1])
        return res

        
    
