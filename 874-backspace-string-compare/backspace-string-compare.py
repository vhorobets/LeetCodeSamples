class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def transformStr(r: str) -> str:
            stack = []
            for i in range(len(r)):
                if r[i] == '#' and stack:
                    stack.pop()
                elif r[i] != '#':
                    stack.append(r[i])

            return ''.join(stack)

        return transformStr(s) == transformStr(t)


