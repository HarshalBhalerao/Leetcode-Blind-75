class Solution:
    def maxArea(self, height: List[int]) -> int:

        def calculateArea(l, r):
            return (min(height[l], height[r])) * (r - l)

        # Creating a variable to keep track of the maxArea
        maxArea = 0

        # Initializing our left and right pointers
        l, r = 0, (len(height) - 1)

        while l < r:
            maxArea = max(calculateArea(l, r), maxArea)

            if height[l] < height[r] and l < r:
                l += 1
            else:
                r -= 1

        return maxArea

