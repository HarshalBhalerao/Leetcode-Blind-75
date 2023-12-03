class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # This is going to be our hashmap where we add all the elements
        map = {}

        # Now we will iterate through those elements.
        for i, n in enumerate(nums):
            # Calculate the difference
            diff = target - n

            # if diff exists in our hashmap then we return the indices.
            if diff in map:
                return [map[diff], i]
            
            # If not then we add that element in our hashmap
            map[n] = i

        return
