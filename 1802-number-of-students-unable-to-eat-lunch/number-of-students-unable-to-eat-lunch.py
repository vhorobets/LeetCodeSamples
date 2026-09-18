from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        queue = deque(students)
        stack = deque(sandwiches)

        currentCount = 0
        currentQueue = len(queue)
        
        while queue and currentCount < currentQueue:
            curr_student = queue.popleft()

            if curr_student == stack[0]:
                stack.popleft()
                currentCount = 0
                currentQueue -= 1
            else:
                queue.append(curr_student)
                currentCount += 1

        return currentQueue