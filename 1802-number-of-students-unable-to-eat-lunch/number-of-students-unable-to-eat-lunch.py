from collections import deque

class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        queue = deque(students)

        sandwich_index = 0
        skipped = 0

        while queue and skipped < len(queue):
            student = queue.popleft()

            if student == sandwiches[sandwich_index]:
                sandwich_index += 1
                skipped = 0
            else:
                queue.append(student)
                skipped += 1

        return len(queue)