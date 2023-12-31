import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

	ops = {
		'+': operator.add,
		'-': operator.sub,
		'*': operator.mul,
		'/': operator.truediv
		}

	for token in tokens:
		if token not in ops:
			stack.append(int(token))
		else:
			n2 = stack.pop()
			n1 = stack.pop()
			result = ops[token](n1, n2)
			stack.append(int(result))
	return stack[0]

# Sol 2 without imports
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Keeps track of numeric characters when we encounter an operator we pop 2 most recent items from the stack and perform the arithemetic operation
        stack = [] 

        # Result
        result = 0

        if len(tokens) == 1:
            return int(tokens[0])

        # Iterate through the list
        for token in tokens:
            if token not in "+-/*": # Numeric character append to stack
                stack.append(token)
            else: # Non-numeric character then perform operation
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = int(num2) + int(num1)
                elif token == "-":
                    result = int(num2) - int(num1)
                elif token == "*":
                    result = int(num2) * int(num1)
                elif token == "/":
                    result = int(num2) / int(num1)

                stack.append(result)
                print(result)

        return int(result)
        