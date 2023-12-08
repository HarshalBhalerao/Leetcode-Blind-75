class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # result array: the one we are going to return our result in
        result = []

        # We will implement Depth-first search
        def dfs(i, current, total):
            # Base case 1: When target is equal to total
            if(total == target):
                result.append(current.copy())
                return
            
            # Base case 2: When we have reached the end of our array or total is greater than our target
            if(i >= len(candidates) or total > target):
                return

            # To the same element again to our current, to check whether we get closer to the target
            current.append(candidates[i])
            # We run dfs back again to check whether it worked
            dfs(i, current, total + candidates[i])

            # Now condition #2, when we change the candidate element itself
            # First we have to pop the appended element
            current.pop()
            # Move to the next element in the candidate array
            dfs(i + 1, current, total)

        # Initialize and call the dfs method
        dfs(0, [], 0)
        return result
            

