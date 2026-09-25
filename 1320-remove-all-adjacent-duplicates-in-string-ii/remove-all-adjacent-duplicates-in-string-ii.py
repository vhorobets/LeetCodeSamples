class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for c in s:
            if not stack:
                stack.append((c, 1))
            else:
                char, count = stack.pop()

                if char == c:
                    count += 1
                    if count != k:
                        stack.append((char, count))
                else:
                    stack.append((char, count))
                    stack.append((c, 1))
        
        return ''.join(char * count for char, count in stack)
