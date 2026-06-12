class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_letters = defaultdict(int)

        for c in magazine:
            magazine_letters[c] += 1

        for c in ransomNote:
            magazine_letters[c] -= 1

            if magazine_letters[c] < 0:
                return False

        return True