class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # ValidParentheses is an array which would keep track of the valid parentheses. Those indices would have 1 value
        validParentheses = [0]*len(s) #Setting the length equal to our string s
        # This stack is to check the validity of the given string
        checkStack = []

        # We will iterate and get the respective indices and its corresponding elements
        for index, char in enumerate(s):
            if "(" in char:
                checkStack.append(index)
            elif ")" in char:
                if checkStack: # If there are elements in the stack then check for a open parentheses
                    # Set the indices of that element to 1
                    validParentheses[checkStack.pop()] = 1
                    validParentheses[index] = 1       
                else:
                    # If stack is empty then do nothing and continue
                    continue
            else:
                # This else statement is for the characters
                continue

        # Result string
        result = ""
        # Iterate through the string s
        for index, character in enumerate(s):
            # If any character is ()
            if character in ")" or character in "(":
                # Check their value in valid parentheses
                if validParentheses[index] == 1:
                    result += character # Append
                else: # Else pass
                    pass
            else: # Else it is a normal alphabet and thus add it to our result string
                result += character
        return result



