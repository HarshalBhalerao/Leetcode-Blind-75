class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This hashmap would keep track of the number of times an element has appeared.
        countOccurence = {}

        # Create a bucket which would keep track of elements which appear specific number of times
        freqBucket = [[] for i in range(len(nums) + 1)]

        # Our result list
        result = []

        for element in nums:
            countOccurence[element] = 1 + countOccurence.get(element, 0)

        # Add the elements to our bucket
        for element, count in countOccurence.items():
            freqBucket[count].append(element)

        # Decrement from the end of the bucket getting the most frequent elements
        for index in range(len(freqBucket) - 1, 0, -1):
            for elements in freqBucket[index]:
                # If element exists then append it to our result
                result.append(elements)
                # Stop when we reach k and return the result 
                if len(result) == k:
                    return result



        

        
