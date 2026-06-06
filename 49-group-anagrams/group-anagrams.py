class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for s in strs:
            s_sorted = str(sorted(s))
            dict[s_sorted].append(s)

        result = []
        for arr in dict.values():
            result.append(arr)

        return result
            