# 788. Rotated Digits
# An integer x is a good if after rotating each digit individually by 180 degrees, we get a valid number that is different from x. Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. For example:

# 0, 1, and 8 rotate to themselves,
# 2 and 5 rotate to each other (in this case they are rotated in a different direction, in other words, 2 or 5 gets mirrored),
# 6 and 9 rotate to each other, and
# the rest of the numbers do not rotate to any other number and become invalid.
# Given an integer n, return the number of good integers in the range [1, n].

 
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.


# Example 2:
# Input: n = 1
# Output: 0
# Example 3:

# Input: n = 2
# Output: 1
 

# Constraints:
# 1 <= n <= 104

#--------------------brute force solution--------------------
class Solution(object):
    def rotatedDigits(self, n):
        count = 0
        
        for num in range(1, n + 1):
            if self.is_good(num):
                count += 1
        
        return count
    
    def is_good(self, num):
        valid_digits = {'0', '1', '8', '2', '5', '6', '9'}
        rotated_digits = {'2': '5', '5': '2', '6': '9', '9': '6'}
        
        num_str = str(num)
        
        for digit in num_str:
            if digit not in valid_digits:
                return False
        
        rotated_num_str = ''.join(rotated_digits.get(digit, digit) for digit in num_str)
        
        return rotated_num_str != num_str
if __name__== "__main__":
    a = Solution()
    n1 = 10
    print(a.rotatedDigits(n1))  # 4

    n2 = 1
    print(a.rotatedDigits(n2))  # 0

    n3 = 2
    print(a.rotatedDigits(n3))  # 1
## Time Complexity: O(n * m) where n is the input integer and m is the average number of digits in the integers from 1 to n. This is because we iterate through each integer from 1 to n and for each integer, we check if it is a good number by iterating through its digits.
## Space Complexity: O(m) where m is the average number of digits in the integers from 1 to n. This is because we create a string representation of each integer to check if it is a good number, and the space used for this string is proportional to the number of digits in the integer.


#--------------------optimized solution--------------------
class Solution:
    def rotatedDigits(self, n):
        count = 0
        
        for num in range(1, n + 1):
            if self.is_good(num):
                count += 1
        
        return count
    
    def is_good(self, num):
        valid_digits = {'0', '1', '8', '2', '5', '6', '9'}
        rotated_digits = {'2': '5', '5': '2', '6': '9', '9': '6'}
        
        has_rotatable_digit = False
        
        while num > 0:
            digit = num % 10
            if str(digit) not in valid_digits:
                return False
            if str(digit) in rotated_digits:
                has_rotatable_digit = True
            num //= 10
        
        return has_rotatable_digit
if __name__== "__main__":
    a = Solution()
    n1 = 10
    print(a.rotatedDigits(n1))  # 4

    n2 = 1
    print(a.rotatedDigits(n2))  # 0

    n3 = 2
    print(a.rotatedDigits(n3))  # 1
## Time Complexity: O(n * m) where n is the input integer and m is the average number of digits in the integers from 1 to n. This is because we iterate through each integer from 1 to n and for each integer, we check if it is a good number by iterating through its digits.
## Space Complexity: O(1) because we are using a constant amount of space to store
# the valid digits and rotated digits, and we are not using any additional space that grows with the input size.
