class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_len = len(s)
        p_len = len(p)
       
        if p_len > s_len:
            return []
       
        p_letter_counts = [0] * 26
       
        for ch in p:
            p_letter_counts[ord(ch) - ord('a')] += 1

        result = []

        windows_letter_counts = [0] * 26

        #init window
        i = 0
        while i < p_len:
            windows_letter_counts[ord(s[i]) - ord('a')] += 1
            i += 1

        if windows_letter_counts == p_letter_counts:
            result.append(0)

        while i < s_len:
            windows_letter_counts[ord(s[i - p_len]) - ord('a')] -= 1
            windows_letter_counts[ord(s[i]) - ord('a')] += 1
            
            if windows_letter_counts == p_letter_counts:
                result.append(i - p_len + 1)
        
            i += 1

        return result
