from typing import List
from collections import Counter
import heapq

# Push all words into a hash table
# Push all words and their freq into a heap
# Pop k words from the heap

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash = Counter(words)
        heap = []
        for word, cnt in hash.items():
            heap.append((-cnt, word))
        heapq.heapify(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res