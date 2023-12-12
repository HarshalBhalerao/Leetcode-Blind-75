class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list) # Return a list containing list of similar anagrams, by mapping charCount to 

        # Go through the input list full of words
        for word in strs:
            # keeps count of character appearance from a to z
            count = [0] * 26 
            # Now go through each of the characters
            for char in word:
                count[ord(char) - ord("a")] += 1

            # List cannot be keys in python, thus we use a tuple
            output[tuple(count)].append(word)
        
        return output.values()
                
        
