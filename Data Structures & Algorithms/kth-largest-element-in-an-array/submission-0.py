class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)

            if len(heap)>k:
                heapq.heappop(heap)

        # for i in range(k-1):
        #     k=heapq.heappop(heap)
        #     print(k)
        return heapq.heappop(heap)