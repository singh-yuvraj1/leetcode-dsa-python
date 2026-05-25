# 1871. Jump Game VII
# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.

 

# Example 1:
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3. 
# In the second step, move from index 3 to index 5.


# Example 2:
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
 

# Constraints:
# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length


#brute force solution--- using bfs---

class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """

        n = len(s)

        def dfs(i):

            # reached last index
            if i == n - 1:
                return True

            # try all possible jumps
            for j in range(i + minJump,
                           min(i + maxJump + 1, n)):

                if s[j] == '0':
                    if dfs(j):
                        return True

            return False

        return dfs(0)
if __name__ == "__main__":
    s = "011010"
    minJump = 2
    maxJump = 3
    print(Solution().canReach(s, minJump, maxJump))  # Output: true
#time complexity: O(n^2) in worst case, where n is the length of the string s. This is because in the worst case, we may have to explore all possible jumps from each index.
#space complexity: O(n) in the worst case, where n is the length of the string s. This is because in the worst case, we may have to store all indices in the call stack due to recursion.


#optimal solution--- using bfs and sliding window technique---
class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """

        n = len(s)

        queue = [0]
        front = 0

        # farthest index already checked
        far = 0

        while front < len(queue):

            i = queue[front]
            front += 1

            start = max(i + minJump, far + 1)
            end = min(i + maxJump, n - 1)

            for j in range(start, end + 1):

                if s[j] == '0':

                    if j == n - 1:
                        return True

                    queue.append(j)

            far = end

        return n == 1
if __name__ == "__main__":
    s = "011010"
    minJump = 2
    maxJump = 3
    print(Solution().canReach(s, minJump, maxJump))  # Output: true
#time complexity: O(n) in the worst case, where n is the length of the string s. This is because we may have to explore all indices in the string.
#space complexity: O(n) in the worst case, where n is the length of the string s. This is because in the worst case, we may have to store all indices in the queue.


