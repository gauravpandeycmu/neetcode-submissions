class Solution:
    def helper(self, grid, row, col):
        directions = [[-1, 0], [0, -1], [1, 0], [0,1]]
        m = len(grid)
        n = len(grid[0])

        for i, j in directions:
            newRow = row + i
            newCol = col + j

            if newRow>=0 and newRow<m and newCol>=0 and newCol<n and grid[newRow][newCol]=="1":
                grid[newRow][newCol] = "0"
                self.helper(grid, newRow, newCol)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    print(i, j)
                    grid[i][j] = "0"
                    count += 1
                    self.helper(grid, i, j)        

        return count

