class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0
        rows = [tuple(row) for row in grid]
        for j in range(n):
            column = tuple(grid[i][j] for i in range(n))
            for row in rows:
                if row == column:
                    count += 1   
        return count