class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the total number of rows and cols
        ROWS, COLS = len(board), len(board[0])
        # Same letter cell may not be used more than once
        path = set()

        def dfs(row, col, curr):
            # Base case #1: If we find the correct set of characters for our word. We return true.
            if curr == len(word):
                return True
            
            # Base case #2: Consider all the edge cases, if the elements don't match or if the same letter cell is being used again then return False
            if (row >= ROWS or col >= COLS or
                row < 0 or col < 0 or
                board[row][col] != word[curr] or 
                (row,col) in path):
                return False 

            # Add row and col to our path
            path.add((row, col))
            # Check the neighbouring nodes to see if we get a part of our word string
            result = (dfs(row - 1, col, curr + 1) or
                    dfs(row + 1, col, curr + 1) or
                    dfs(row, col - 1, curr + 1) or 
                    dfs(row, col + 1, curr + 1))
            # If it is not the right one we backtrack and remove that path from our set
            path.remove((row,col))
            return result

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0): return True
        return False

