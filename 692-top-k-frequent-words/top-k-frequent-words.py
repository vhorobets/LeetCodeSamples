import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = Counter(words)

        # Sort by: frequency descending, word ascending
        result = sorted(counts.keys(), key=lambda w: (-counts[w], w))

        return result[:k]
            