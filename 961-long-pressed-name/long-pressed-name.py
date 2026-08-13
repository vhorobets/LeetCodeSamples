class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                continue
            else:
                return False

        return i == len(name)