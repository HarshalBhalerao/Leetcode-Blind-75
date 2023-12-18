class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialize and fill the array result with 1's [1,1,1,1,...]
        result = [1] * (len(nums))

        # The left side of nums[0] is nothing so we want that to be 1
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # The right side of nums[-1] is nothing so we want that to be 1
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result

