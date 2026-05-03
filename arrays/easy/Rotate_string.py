# 796. Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.
 

# Example 1:
# Input: s = "abcde", goal = "cdeab"
# Output: true


# Example 2:
# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

#solution 1: Brute Force Solution
class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            s = s[1:] + s[0]  # Rotate the string by moving the leftmost character to the rightmost position
            if s == goal:
                return True
        
        return False
if __name__== "__main__":
    a = Solution()
    s1, goal1 = "abcde", "cdeab"
    print(a.rotateString(s1, goal1))  # True

    s2, goal2 = "abcde", "abced"
    print(a.rotateString(s2, goal2))  # False
## Time Complexity: O(n^2) where n is the length of the input string. We have a loop that iterates n times, and for each iteration, we perform a string rotation which takes O(n) time.
## Space Complexity: O(1) since we are not using any additional data structures that grow with the input size. We are only using a constant amount of space for the loop variable and the return value.
