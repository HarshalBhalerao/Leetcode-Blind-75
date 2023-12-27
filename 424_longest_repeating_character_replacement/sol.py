class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 # Left Pointer

        # Hashmap to keep track of the count of the elements
        countHashmap = {}
        result = 0 # Resulting maximum length of our window
        maxCount = 0 # Resulting maximum count

        for right in range(len(s)):
            # Once we encounter an element we increment its count
            countHashmap[s[right]] = 1 + countHashmap.get(s[right], 0)
            maxCount = max(maxCount, countHashmap[s[right]])

            # Validate the window by calculating using this formula
            if (right - left + 1) - maxCount > k:
                # If window is invalid, decrement the count of that element
                countHashmap[s[left]] -= 1
                # Update the position of left pointer
                left += 1

            # Calculate the max valid window size 
            result = max(result, (right - left + 1))

        return result
            


