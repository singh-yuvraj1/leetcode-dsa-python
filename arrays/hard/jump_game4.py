# 1345. Jump Game IV
# Given an array of integers arr, you are initially positioned at the first index of the array.
# In one step you can jump from index i to index:

# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# Return the minimum number of steps to reach the last index of the array.

# Notice that you can not jump outside of the array at any time.

 

# Example 1:

# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.


# Example 2:
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You do not need to jump.


# Example 3:
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

# Constraints:
# 1 <= arr.length <= 5 * 104
# -108 <= arr[i] <= 108
 

#brute force---
class Solution:
    def minJumps(self, arr):
        from collections import deque

        n = len(arr)
        if n == 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] not in graph:
                graph[arr[i]] = []
            graph[arr[i]].append(i)

        visited = set()
        queue = deque([(0, 0)])  # (index, steps)
        visited.add(0)

        while queue:
            index, steps = queue.popleft()

            # Check if we have reached the last index
            if index == n - 1:
                return steps

            # Explore neighbors
            neighbors = [index + 1, index - 1] + graph.get(arr[index], [])
            for neighbor in neighbors:
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

            # Clear the list to prevent future redundant checks
            graph[arr[index]] = []

        return -1  # If we cannot reach the last index
if __name__ == "__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    print(Solution().minJumps(arr))
#output: 3
#time complexity: O(n) because in the worst case, we may visit each index of the array once.
#space complexity: O(n) because in the worst case, we may have to store all indices in the visited set and the graph.


#optimal solution---
class Solution1:
    def minJumps(self, arr):
        from collections import deque

        n = len(arr)
        if n == 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] not in graph:
                graph[arr[i]] = []
            graph[arr[i]].append(i)

        visited = set()
        queue = deque([(0, 0)])  # (index, steps)
        visited.add(0)

        while queue:
            index, steps = queue.popleft()

            # Check if we have reached the last index
            if index == n - 1:
                return steps

            # Explore neighbors
            neighbors = [index + 1, index - 1] + graph.get(arr[index], [])
            for neighbor in neighbors:
                if 0 <= neighbor < n and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, steps + 1))

            # Clear the list to prevent future redundant checks
            graph[arr[index]] = []

        return -1  # If we cannot reach the last index
if __name__ == "__main__":
    arr = [100,-23,-23,404,100,23,23,23,3,404]
    print(Solution1().minJumps(arr))
#output: 3
#time complexity: O(n) because in the worst case, we may visit each index of the array once.
#space complexity: O(n) because in the worst case, we may have to store all indices in the visited set and the graph.
