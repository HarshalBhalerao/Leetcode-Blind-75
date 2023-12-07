class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Hashmap for mapping each closing bracket to its respective opening one
        closeToOpen = { "}" : "{", ")" : "(", "]" : "["}

        # Go through each char in the string
        for c in s:
            # If the char belongs to our hashmap
            if c in closeToOpen:
                # Check if stack is not null and if the last element in our stack is equal to the respective element in hashmap, we pop from stack
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            # If that char isn't in our stack then we append
            else:
                stack.append(c)

        # Return true only if stack is empty, else False
        return True if not stack else False
        
