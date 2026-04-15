class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the freq of elements: num -> freq
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # add tuples of freq -> num to min heap, pop when exceed k elements
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # return list of min_heap[i][1] elements
        return [tup[1] for tup in min_heap]