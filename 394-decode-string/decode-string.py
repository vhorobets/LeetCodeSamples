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