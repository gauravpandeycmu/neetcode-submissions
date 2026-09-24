class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        
        for val, count in map.items():
            freq[count].append(val)

        res = []
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res)==k:
                    return res
        return res
    