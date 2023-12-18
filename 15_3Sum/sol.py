class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        # First step is to sort this array as we are bound to meet duplicates
        nums.sort()

        # Iterate through this array
        for index, num in enumerate(nums):
            # If a previous index already exists and if that value and this one is the same then move to the next position
            if index > 0 and nums[index - 1] == nums[index]:
                continue # We move to the next iteration
            
            l, r = index + 1, (len(nums) - 1)
            while l < r:
                sum = nums[index] + nums[l] + nums[r]

                # If all these sum to 0, then we got our result. Thus, we return it
                if sum == 0:
                    # Append it to our result
                    result.append([nums[index], nums[l], nums[r]])
                    # Make sure to update the left pointer and left pointer should be less than right pointer.
                    if l < r:
                        l += 1
                    # Now update the left pointer and make sure it is less than right
                    # Also we need to consider when we update the left pointer that the previous left pointer is not equal to the current left pointer value.
                    while nums[l] == nums[l - 1] and l < r: 
                        l += 1
                elif sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1

        return result if result else []


        
