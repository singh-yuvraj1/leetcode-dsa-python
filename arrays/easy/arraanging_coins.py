# 441. Arranging Coins
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.
# Given the integer n, return the number of complete rows of the staircase you will build.

 
# Example 1:

# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.


# Example 2:

# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1

#brute force solution = O(n) time complexity and O(1) space complexity
def arrangeCoins(n):
    k = 0
    while n >= k + 1:
        k += 1
        n -= k
    return k
if __name__ == "__main__":
    n = 5
    print(arrangeCoins(n))  # Output: 2


#time complexity = O(n)  because we are iterating through the number of coins until we can no longer form a complete row
#space complexity = O(1)  because we are using a constant amount of space 


#optimized solution = O(log n) time complexity and O(1) space complexity
def arrangeCoins(n):
    left, right = 0, n
    while left <= right:
        mid = left + (right - left) // 2
        curr = mid * (mid + 1) // 2
        if curr == n:
            return mid
        if curr < n:
            left = mid + 1
        else:
            right = mid - 1
    return right
if __name__ == "__main__":
    n = 5
    print(arrangeCoins(n))  # Output: 2
#time complexity = O(log n)  because we are using binary search to find the number of complete rows
#space complexity = O(1)  because we are using a constant amount of space
