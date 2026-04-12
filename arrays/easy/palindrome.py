# 9. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:
# -231 <= x <= 231 - 1

# solution 1     brute force approach
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        original = x
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x = x // 10

        return original == rev
if __name__== "__main__":
    a = Solution()
    print(a.isPalindrome(121))  # True
    print(a.isPalindrome(-121)) # False
    print(a.isPalindrome(10))   # False
 

#  `time complexity: O(log10(n)) - We are reversing the number, which takes O(log10(n)) time where n is the input number. This is because we are dividing the number by 10 in each iteration.
#  space complexity: O(1) - We are using a constant amount of extra space to store    


# approach 2  two pointer approach
class Solution2(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        str_x = str(x)
        left, right = 0, len(str_x) - 1
        
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        
        return True     
if __name__== "__main__":
    a = Solution2()
    print(a.isPalindrome(121))  # True
    print(a.isPalindrome(-121)) # False
    print(a.isPalindrome(10))   # False

#time complexity: O(n) - We are converting the number to a string and then using two pointers to check for palindrome, which takes O(n) time where n is the number of digits in the input number.
#space complexity: O(n) - We are converting the number to a string, which takes O(n) space where n is the number of digits in the input number.