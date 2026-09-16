class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def explore(x, y):
            # Stop condition
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return
            
            if grid[x][y] != "1":
                return

            # Visited
            grid[x][y] = 0

            # Explore up
            explore(x + 1, y)
            
            # Explore left
            explore(x, y - 1)

            # Explore right
            explore(x, y + 1)

            # Explore down
            explore(x - 1, y)


        islands = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    islands += 1
                    explore(x, y)

        return islands