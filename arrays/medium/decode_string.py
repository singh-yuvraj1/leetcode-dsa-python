# 394. Decode String
# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"


# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"


# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
 

# Constraints:
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1,300].




# brute force solution
class Solution:
    def decodeString(self, s: str) -> str:

        def helper(i):
            result = ""
            num = 0

            while i < len(s):

                if s[i].isdigit():
                    num = num * 10 + int(s[i])

                elif s[i] == '[':
                    decoded, i = helper(i + 1)
                    result += num * decoded
                    num = 0

                elif s[i] == ']':
                    return result, i

                else:
                    result += s[i]

                i += 1

            return result, i

        ans, _ = helper(0)
        return ans
if __name__ == "__main__":
    a = Solution()
    s1 = "3[a]2[bc]"
    print(a.decodeString(s1))  # Output: "aaabcbc"

    s2 = "3[a2[c]]"
    print(a.decodeString(s2))  # Output: "accaccacc"

    s3 = "2[abc]3[cd]ef"
    print(a.decodeString(s3))  # Output: "abcabccdcdcdef"
# time complexity: O(n) - We traverse the input string once, where n is the length of the string.
# space complexity: O(m) - The space complexity is O(m), where m is the maximum depth of nested brackets in the input string. This is because we use a recursive helper function that can go as deep as the number of nested brackets. In the worst case, if there are many nested brackets, the space used by the call stack can grow accordingly.



#optimized solution using stack

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            elif ch == '[':
                stack.append((curr_str, curr_num))
                curr_str = ""
                curr_num = 0

            elif ch == ']':
                prev_str, num = stack.pop()
                curr_str = prev_str + num * curr_str

            else:
                curr_str += ch

        return curr_str
if __name__ == "__main__":
    a = Solution()
    s1 = "3[a]2[bc]"
    print(a.decodeString(s1))  # Output: "aaabcbc"

    s2 = "3[a2[c]]"
    print(a.decodeString(s2))  # Output: "accaccacc"

    s3 = "2[abc]3[cd]ef"
    print(a.decodeString(s3))  # Output: "abcabccdcdcdef"
# time complexity: O(n) - We traverse the input string once, where n is the length of the string.
# space complexity: O(m) - The space complexity is O(m), where m is the maximum depth of nested brackets in the input string. This is because we use a stack to keep track of the previous strings and numbers, and in the worst case, if there are many nested brackets, the stack can grow accordingly.
