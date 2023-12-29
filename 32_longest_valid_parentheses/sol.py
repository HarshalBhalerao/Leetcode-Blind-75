class Solution:
    def longestValidParentheses(self, s: str) -> int:
        validStack = []
        validParentheses = [0]*len(s)

        # String is empty thus return 0
        if s == "":
            return 0

        # Go through each character in string s
        for index, character in enumerate(s):
            if character == "(":
                # If the character is a open bracket then add its index to the stack
                validStack.append(index)
            if character == ")":
                # But if it is a closed bracket then we evaluate
                if validStack:
                    # If the stack is not empty, then we pop the most recent value added to the stack, and set its index and its closing bracket index in validParentheses to 1
                    validParentheses[validStack.pop()] = 1
                    validParentheses[index] = 1
                else:
                    # If stack is empty, then pass
                    pass


        # Iterate the validParentheses stack to find the longest substring with valid parentheses
        count = 0
        maxCount = 0
        for index, character in enumerate(validParentheses):
            if character == 1:
                count += 1
                maxCount = max(maxCount, count)
            else: 
                count = 0

        return maxCount
            