class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hash = defaultdict(int)

        for n in arr:
            hash[n] += 1

        max = -1

        for key in hash:
            if hash[key] == key and key > max:
                max = key
        
        return max