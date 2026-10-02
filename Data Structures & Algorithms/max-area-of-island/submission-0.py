class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def checkArea(row, col, area):
            grid[row][col] = 0
            totalArea = 1

            for direction in directions:
                newRow = row + direction[0]
                newCol = col + direction[1]

                if newRow>=0 and newRow<ROWS and newCol>=0 and newCol<COLS and grid[newRow][newCol]:
                    totalArea += checkArea(newRow, newCol, area+1)
            return totalArea
        area = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col]:
                    temp = 1
                    area = max(area, checkArea(row, col, temp))

        return area