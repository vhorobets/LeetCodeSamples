class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        result = []

        current = intervals[0]
        n = len(intervals)

        if n == 1:
            result.append(current)

        for i in range(1, n):
            next = intervals[i]

            if self.__is__overlapping(current, next):
                current = self.__merge__intervals(current, next)
            else:
                result.append(current)
                current = next

            if i == n - 1:
                result.append(current)

        return result

    def __is__overlapping(self, int1: List[int], int2: List[int]) -> bool:
        return int1[0] <= int2[1] and int2[0] <= int1[1]

    def __merge__intervals(self, int1: List[int], int2: List[int]) -> List[int]:
        return [min(int1[0], int2[0]), max(int1[1], int2[1])]