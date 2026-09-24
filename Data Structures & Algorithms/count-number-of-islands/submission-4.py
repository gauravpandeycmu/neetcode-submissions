class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [0, -1], [1, 0], [0,1]]
        ROWS, COLS = len(grid), len(grid[0])

        count = 0

        def dfs(row, col):
            for i, j in directions:
                newRow = row + i
                newCol = col + j

                if newRow>=0 and newRow<ROWS and newCol>=0 and newCol<COLS and grid[newRow][newCol]=="1":
                    grid[newRow][newCol] = "0"
                    dfs(newRow, newCol)

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    print(i, j)
                    grid[i][j] = "0"
                    count += 1
                    dfs(i, j)        

        return count

