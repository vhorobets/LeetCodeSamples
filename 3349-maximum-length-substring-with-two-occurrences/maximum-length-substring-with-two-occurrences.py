class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = defaultdict(int)

        max_lenght = 0
        left = 0

        for right in range(len(s)):
            counter[s[right]] += 1

            while counter[s[right]] > 2:
                counter[s[left]] -= 1
                left += 1

            max_lenght = max(max_lenght, right - left + 1)

        return max_lenght