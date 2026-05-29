class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        result = []

        overlap = False
        i = 0
        while i < len(intervals):
            if not self.__is__overlapping(intervals[i], newInterval):
                result.append(intervals[i])
                i += 1
            else:
                overlap = True
                overlapedIntervals = [newInterval]
                while i < len(intervals) and self.__is__overlapping(intervals[i], newInterval):
                    overlapedIntervals.append(intervals[i])
                    i += 1
                
                result.append(self.__merge__intervals(overlapedIntervals))

        # no overlap, need just insert new interval at proper place
        if not overlap:
            a, b, n = newInterval[0], newInterval[1], len(intervals)
            # beggining
            if a < intervals[0][0]:
                result.insert(0, newInterval)
            elif a > intervals[n - 1][0]:
                result.insert(n, newInterval)
            else:
                i = 0
                while intervals[i][0] < a:
                    i += 1

                result.insert(i, newInterval)

        return result

    def __is__overlapping(self, int1: List[int], int2: List[int]) -> bool:
        return int1[0] <= int2[1] and int2[0] <= int1[1]

    def __merge__intervals(self, intervals: List[List[int]]) -> List[int]:
        min, max = intervals[0][0], intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < min:
                min = intervals[i][0]
            if intervals[i][1] > max:
                max = intervals[i][1]

        return [min, max]