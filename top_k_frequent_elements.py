from typing import List
import collections
import heapq

class Solution():

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freqs = collections.Counter(nums)

        freqs_heap = []

        for f in freqs:
            heapq.heappush(freqs_heap, (-freqs[f], f))

        topk = []
        for _ in range(k):
            topk.append(heapq.heappop(freqs_heap)[1])

        return topk


if __name__ == "__main__":
    input = [1, 1, 1, 2, 2, 3]
    k = 2

    sol = Solution()
    print(sol.topKFrequent(input, k))