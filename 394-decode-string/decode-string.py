class Solution:
    def decodeString(self, s: str) -> str:
        
        def decodePart(i):
            res = ''

            while i < len(s) and s[i] != ']':
                if s[i].isdigit():
                    # 1. Read number
                    k = 0
                    while s[i].isdigit():
                        k = k * 10 + int(s[i])
                        i += 1

                    # i is at '['
                    i += 1

                    # 2. Decode everything inside [...]
                    decoded, i = decodePart(i)

                    # 3. i is at ']'
                    i += 1

                    res += decoded * k

                else:
                    res += s[i]
                    i += 1

            return res, i

        result, _ = decodePart(0)
        return result

# Example: "3[a2[c]]"
#
# decodePart(0):
#   k = 3
#   skip '['
#   -> decodePart(2)
#
#     res = "a"
#     k = 2
#     skip '['
#     -> decodePart(5)
#
#         res = "c"
#         hit ']'
#         return ("c", i)
#
#     decoded = "c"
#     res = "a" + "c" * 2 = "acc"
#     hit ']'
#     return ("acc", i)
#
# decoded = "acc"
# res = "acc" * 3 = "accaccacc"
#
# Each recursive call decodes one nesting level.
# When it hits ']', it returns the decoded string
# and the current index back to the previous level.