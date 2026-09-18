class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        minHeap = []
        for elem, f in count.items():
            heapq.heappush(minHeap, (f, elem))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res