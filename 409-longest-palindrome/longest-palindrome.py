class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for c in s:
            counts[c] = counts[c] + 1

        result = 0
        has_odd = False
        for cnt in counts.values():
            if cnt % 2 == 0:
                result = result + cnt
            else:
                result = result + cnt - 1
                has_odd = True

        return result + 1 if has_odd else result