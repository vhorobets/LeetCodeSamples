class Solution(object):
    def isValid(self, s):
        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                lastInStack = stack.pop()

                if ((c == ')' and lastInStack == '(') or
                (c == '}' and lastInStack == '{') or
                (c == ']' and lastInStack == '[')):
                    continue
                else:
                    return False

        return len(stack) == 0
        