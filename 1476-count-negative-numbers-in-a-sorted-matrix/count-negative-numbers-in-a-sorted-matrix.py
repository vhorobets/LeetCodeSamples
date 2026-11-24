class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
    #    4  3  2 -1
    #    3  2  1 -1
    #    1  1 -1 -2
    #   -1 -1 -2 -3

        count_negative = 0
        
        row, col = 0, len(grid[0]) - 1
        
        while col >= 0 and row < len(grid):
            if grid[row][col] < 0:
                count_negative += len(grid) - row
                col -= 1
            else:
                row += 1

        return count_negative