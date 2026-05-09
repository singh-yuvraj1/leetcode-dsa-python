# 3783. Mirror Distance of an Integer

# You are given an integer n.
# Define its mirror distance as: abs(n - reverse(n))​​​​​​​ where reverse(n) is the integer formed by reversing the digits of n.
# Return an integer denoting the mirror distance of n​​​​​​​.
# abs(x) denotes the absolute value of x.

 
# Example 1:
# Input: n = 25
# Output: 27
# Explanation:

# reverse(25) = 52.
# Thus, the answer is abs(25 - 52) = 27.


# Example 2:
# Input: n = 10
# Output: 9
# Explanation:

# reverse(10) = 01 which is 1.
# Thus, the answer is abs(10 - 1) = 9.


# Example 3:
# Input: n = 7
# Output: 0
# Explanation:

# reverse(7) = 7.
# Thus, the answer is abs(7 - 7) = 0.
 

# Constraints:
# 1 <= n <= 109

# Solution 1: Brute Force Solution
class Solution(object):
    def mirrorDistance(self, n):
        def reverse(num):
            return int(str(num)[::-1])
        
        return abs(n - reverse(n))
if __name__== "__main__":
    a = Solution()
    n1 = 25
    print(a.mirrorDistance(n1))  # 27

    n2 = 10
    print(a.mirrorDistance(n2))  # 9

    n3 = 7
    print(a.mirrorDistance(n3))  # 0
## Time Complexity: O(d) where d is the number of digits in the input integer n. The reverse function takes O(d) time to reverse the digits of n.
## Space Complexity: O(d) due to the space used to store the string representation of n in the reverse function. The space used for the reversed string is proportional to the number of digits in n.