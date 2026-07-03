class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        map = defaultdict(int)

        for i in nums:
            map[i] = map.get(i, 0) + 1

        for i, j in map.items():
            heapq.heappush(maxHeap, (-j, i))

        res = []
        for i in range(k):
            freq, ele = heapq.heappop(maxHeap)
            res.append(ele)

        return res