# 224. Basic Calculator
# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 
# Example 1:
# Input: s = "1 + 1"
# Output: 2


# Example 2:
# Input: s = " 2-1 + 2 "
# Output: 3


# Example 3:
# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
 

# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.


#brute force
class Solution(object):

    def calculate(self, s):

        def solve(exp):

            stack = []
            num = 0
            sign = '+'
            i = 0

            while i < len(exp):

                ch = exp[i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                # Solve bracket recursively
                if ch == '(':
                    count = 1
                    j = i + 1

                    while j < len(exp):
                        if exp[j] == '(':
                            count += 1
                        elif exp[j] == ')':
                            count -= 1

                        if count == 0:
                            break

                        j += 1

                    num = solve(exp[i + 1:j])
                    i = j

                if ch in '+-' or i == len(exp) - 1:

                    if sign == '+':
                        stack.append(num)
                    elif sign == '-':
                        stack.append(-num)

                    sign = ch
                    num = 0

                i += 1

            return sum(stack)

        return solve(s.replace(" ", ""))
if __name__ == "__main__":
    s = Solution()
    print(s.calculate("1 + 1"))  # return 2
    print(s.calculate(" 2-1 + 2 "))  # return 3
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))  # return 23  
# The time complexity of this solution is O(n^2) in the worst case, where n is the length of the input string s. This is because in the worst case, we may have to solve nested brackets recursively, leading to a quadratic number of operations. The space complexity is O(n) due to the stack used for storing intermediate results and the recursive call stack for solving nested brackets.
#space complexity: O(n) due to the stack used for storing intermediate results and the recursive call stack for solving nested brackets.


#optimized solution using stack
class Solution(object):

    def calculate(self, s):

        stack = []
        num = 0
        sign = 1
        result = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in '+-':
                result += sign * num
                sign = 1 if ch == '+' else -1
                num = 0

            elif ch == '(':
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ')':
                result += sign * num
                result *= stack.pop()  # sign before the bracket
                result += stack.pop()  # result calculated before the bracket
                num = 0

        return result + sign * num
if __name__ == "__main__":
    s = Solution()
    print(s.calculate("1 + 1"))  # return 2
    print(s.calculate(" 2-1 + 2 "))  # return 3
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))  # return 23
# The time complexity of this solution is O(n), where n is the length of the input string s. We traverse the string once, and each operation (pushing/popping from the stack) takes O(1) time. The space complexity is O(n) in the worst case, due to the stack used for storing intermediate results when we encounter nested brackets.
#space complexity: O(n) in the worst case, due to the stack used for storing intermediate results when we encounter nested brackets.
