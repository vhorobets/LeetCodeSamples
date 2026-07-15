class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome, such as "abcba"
            odd = self.__extract_palindron(s, i, i)

            if len(odd) > len(longest):
                longest = odd

            # Even-length palindrome, such as "abba"
            even = self.__extract_palindron(s, i, i + 1)

            if len(even) > len(longest):
                longest = even

        return longest
    
    def __extract_palindron(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]