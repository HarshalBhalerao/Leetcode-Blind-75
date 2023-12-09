class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # We check if the two strings are equal. If they aren't then they are not anagrams
        if len(s) != len(t):
            return False

        # We use hashmaps to solve this problem. Get count of each character and then compare both hashmaps
        sHashmap, tHashmap = {}, {}

        # We go through each hashmap
        for index in range(len(s)):
            # We add the count of each character into our hashmap 
            # Use .get() to check if that character exists in our hashmap and get its count, if not then return 0 as default value
            sHashmap[s[index]] = 1 + sHashmap.get(s[index], 0)
            tHashmap[t[index]] = 1 + tHashmap.get(t[index], 0)

        # We iterate through both the hashmaps to check if they are equal
        for character in sHashmap:
            if sHashmap[character] != tHashmap.get(character, 0):
                return False


        return True
        
