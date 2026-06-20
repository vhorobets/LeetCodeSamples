class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_hash = defaultdict(int)

        for c in chars:
            char_hash[c] += 1

        res = 0

        for word in words:
            current_hash = defaultdict(int)

            for c in word:
                current_hash[c] += 1

            good_word = True
            for key in current_hash:
                if key in char_hash and current_hash[key] <= char_hash[key]:
                    continue
                else:
                    good_word = False
                
            if good_word:
                res += len(word)

        return res