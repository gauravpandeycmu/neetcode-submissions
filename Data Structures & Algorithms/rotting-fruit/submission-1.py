class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten = deque()
        fresh = 0

        ROWS = len(grid)
        COLS = len(grid[0])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 2:
                    rotten.append([row, col])
                if grid[row][col] == 1:
                    fresh += 1
        count = 0

        if fresh == 0:
            return 0

        while (rotten and fresh>0):
            print(rotten)
            length = len(rotten)
            count+= 1

            for z in range(length):
                rot = rotten.popleft()

                for i, j in directions:
                    newRow = rot[0] + i
                    newCol = rot[1] + j

                    if newRow>=0 and newCol>=0 and newRow<ROWS and newCol<COLS and grid[newRow][newCol]==1:
                        grid[newRow][newCol] = 2
                        rotten.append([newRow, newCol])
                        fresh -= 1
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    return -1

        return count if fresh==0 else -1
