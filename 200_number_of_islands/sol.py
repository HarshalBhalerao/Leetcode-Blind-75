class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Check if the grid exists
        if not grid:
            return False

        # Get the rows and cols length
        ROWS, COLS = len(grid), len(grid[0])
        # Visit set is going to keep track of visited land position nodes
        visit = set()
        islands = 0

        # Our BFS Method
        def bfs(row, col):
            # First we need to add this node to our queue and search for its neighbouring land nodes
            queue = collections.deque()
            queue.append((row, col))
            # We mark it visited
            visit.add((row, col))

            # While queue not empty
            while queue:
                # Create a directions list to visit neighbouring nodes
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

                # We pop from the left of the queue (If we just have a normal pop function instead of popleft then it is iterative dfs)
                row, col = queue.popleft()

                for neighbourRow, neighbourCol in directions:
                    newRow = row + neighbourRow
                    newCol = col + neighbourCol
                    # We check the validity of that position and check if it is land position and whether it has been added to our visit list. If not then we add it to our queue and visit set
                    if (newRow in range(ROWS) and
                        newCol in range(COLS) and
                        grid[newRow][newCol] == "1" and
                        (newRow, newCol) not in visit):
                        queue.append((newRow, newCol))
                        visit.add((newRow, newCol))


        # We go through the entire grid list and check for a "1" or land position
        for row in range(ROWS):
            for col in range(COLS):
                # If we find a land position and it hasn't been visited
                if grid[row][col] == "1" and (row, col) not in visit:
                    # Send it to bfs to check for neighbouring land nodes
                    bfs(row, col)
                    # Increment the number of islands
                    islands = islands + 1
        
        return islands
