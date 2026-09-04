import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        class WordFrequency:
            def __init__(self, word, freq):
                self.word = word
                self.freq = freq

            def __lt__(self, other): # lower then for comparision in heap
                # Lower frequency is worse
                if self.freq != other.freq:
                    return self.freq < other.freq

                # For same frequency, lexicographically larger is worse
                return self.word > other.word
        
        counts = Counter(words)
        heap = []

        for word, freq in counts.items():
            heapq.heappush(heap, WordFrequency(word, freq))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap).word)

        return result[::-1]
            