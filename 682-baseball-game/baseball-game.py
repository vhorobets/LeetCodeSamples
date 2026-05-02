class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            op = operations[i]

            if op == 'C':
                prev = stack.pop()
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == '+':
                prev1 = stack[-1]
                prev2 = stack[-2]
                stack.append(prev1 + prev2)
            else:
                stack.append(int(op))

        return sum(stack)

