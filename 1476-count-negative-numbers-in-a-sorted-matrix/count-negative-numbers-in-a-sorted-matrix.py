class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
    #    4  3  2 -1
    #    3  2  1 -1
    #    1  1 -1 -2
    #   -1 -1 -2 -3

        count_negative = 0
        for i in range(len(grid)):
            l, r = 0, len(grid[i]) - 1

            while l <= r:
                mid = l + (r - l) // 2

                if grid[i][mid] >= 0:
                    l = mid + 1
                else:
                    r = mid - 1

            count_negative += len(grid[i]) - l

        return count_negative