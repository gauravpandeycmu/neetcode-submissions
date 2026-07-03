class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = Counter(nums)

        maxHeap = [(-freq, ele) for ele, freq in map.items()]
        heapq.heapify(maxHeap)

        return [heapq.heappop(maxHeap)[1] for _ in range(k)]