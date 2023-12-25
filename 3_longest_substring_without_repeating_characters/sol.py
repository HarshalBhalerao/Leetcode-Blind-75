class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hashset would store the unique substring as we are iterating through string s
        hashset = set()
        # Left pointer
        left = 0

        # Result variable - holds the longest substring length with unique characters
        resultLen = 0

        # Make right pointer iterate through all the characters in the str
        for right in range(len(s)):
            # If the character (right pointer is on) is in the hashset, then we remove that character in the hashset and the ones following it until we have a unique substring. Also, update the position of the left pointer.
            while(s[right] in hashset):
                hashset.remove(s[left])
                left += 1
            
            # Add any new unique character to our hashset
            hashset.add(s[right])
            # Because we are ensuring that our hashset always contains unique elements, this ensures that we have a contiguous substring of unique elements. Thus we can find its length and use max function to get the largest value.
            resultLen = max(resultLen, right - left + 1)
        
        return resultLen
