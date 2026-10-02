class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])

        pacVisited = [[0] * COLS for _ in range(ROWS)]
        atlVisited = [[0] * COLS for _ in range(ROWS)]
        print(pacVisited)

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]

        def dfs(row, col, visited):
            visited[row][col] = 1

            for i, j in directions:
                newRow = row + i
                newCol = col + j

                if newRow>=0 and newCol>=0 and newRow<ROWS and newCol<COLS and not visited[newRow][newCol] and heights[newRow][newCol]>=heights[row][col]:
                    dfs(newRow, newCol, visited)

        for row in range(ROWS):
            dfs(row, 0, pacVisited)
            dfs(row, COLS-1, atlVisited)

        for col in range(COLS):
            dfs(0, col, pacVisited)
            dfs(ROWS-1, col, atlVisited)

        res = list()

        for row in range(ROWS):
            for col in range(COLS):
                if atlVisited[row][col] and pacVisited[row][col]:
                    res.append([row, col])
        
        return res