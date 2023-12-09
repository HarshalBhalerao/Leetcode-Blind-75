class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # To solve this problem with time: O(n) and space: O(n)
        
        # We need to use hashmap
        hashmap = {}

        for index, num in enumerate(nums):
            if num in hashmap:
                return True
            hashmap[num] = index
        return False

        # Another solution is using hashset
        hashset = set()

        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


