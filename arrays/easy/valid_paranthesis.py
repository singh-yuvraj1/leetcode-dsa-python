# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:
# Input: s = "()"
# Output: true


# Example 2:
# Input: s = "()[]{}"
# Output: true


# Example 3:
# Input: s = "(]"
# Output: false


# Example 4:
# Input: s = "([])"
# Output: true


# Example 5:
# Input: s = "([)]"
# Output: false

 
# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

#solution 1: Brute Force Solution
class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # If it's a closing bracket
                top_element = stack.pop() if stack else '#'  # Get the top element of the stack or a dummy value
                if mapping[char] != top_element:  # Check if it matches the corresponding opening bracket
                    return False
            else:
                stack.append(char)  # If it's an opening bracket, push it onto the stack
        
        return not stack  # If the stack is empty, all brackets are valid
if __name__== "__main__":
    a = Solution()
    s1 = "()"
    print(a.isValid(s1))  # True

    s2 = "()[]{}"
    print(a.isValid(s2))  # True

    s3 = "(]"
    print(a.isValid(s3))  # False

    s4 = "([])"
    print(a.isValid(s4))  # True

    s5 = "([)]"
    print(a.isValid(s5))  # False
#time complexity: O(n), where n is the length of the string s. We traverse the string once.
#space complexity: O(n), in the worst case, if all characters in the string are

