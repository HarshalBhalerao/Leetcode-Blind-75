class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We require a hashmap
        hashmap = {}

        # We go through the nums array and get the element with its respective index
        for index, num in enumerate(nums):
            # Calculate the difference between target and num
            diff = target - num
            # Check if that difference exists in our hashmap
            if diff in hashmap:
                # If it does then return the index of both
                return [hashmap[diff], index]
            # Else we add that element to the hashmap with its index
            hashmap[num] = index
        return
            
