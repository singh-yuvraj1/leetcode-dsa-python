# 2833. Furthest Point From Origin
# You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.
# In the ith move, you can choose one of the following directions:
# move to the left if moves[i] = 'L' or moves[i] = '_'
# move to the right if moves[i] = 'R' or moves[i] = '_'
# Return the distance from the origin of the furthest point you can get to after n moves.

 

# Example 1:

# Input: moves = "L_RL__R"
# Output: 3
# Explanation: The furthest point we can reach from the origin 0 is point -3 through the following sequence of moves "LLRLLLR".


# Example 2:

# Input: moves = "_R__LL_"
# Output: 5
# Explanation: The furthest point we can reach from the origin 0 is point -5 through the following sequence of moves "LRLLLLL".


# Example 3:

# Input: moves = "_______"
# Output: 7
# Explanation: The furthest point we can reach from the origin 0 is point 7 through the following sequence of moves "RRRRRRR".
 

# Constraints:
# 1 <= moves.length == n <= 50
# moves consists only of characters 'L', 'R' and '_'.


#----------------------------------Brute Force Solution----------------------------------
class Solution(object):
    def furthestDistanceFromOrigin(self, moves):
        left_moves = moves.count('L')
        right_moves = moves.count('R')
        underscore_moves = moves.count('_')
        
        # The furthest point we can reach is the maximum of the left and right moves plus the number of underscore moves
        return max(left_moves, right_moves) + underscore_moves
if __name__== "__main__":
    a = Solution()
    moves1 = "L_RL__R"
    print(a.furthestDistanceFromOrigin(moves1))  # 3

    moves2 = "_R__LL_"
    print(a.furthestDistanceFromOrigin(moves2))  # 5

    moves3 = "_______"
    print(a.furthestDistanceFromOrigin(moves3))  # 7    

## Time Complexity: O(n) where n is the length of the input string moves. We need to iterate through the string once to count the occurrences of 'L', 'R', and '_'.
## Space Complexity: O(1) since we are using a constant amount of extra space to store the counts of 'L', 'R', and '_'.


#----------------------------------Optimal Solution ----------------------------------

class Solution1(object):
    def furthestDistanceFromOrigin(self, moves):
        position = 0
        max_distance = 0

        for move in moves:
            if move == 'L':
                position -= 1
            elif move == 'R':
                position += 1
            # '_' can be treated as either 'L' or 'R', so we consider the maximum possible distance

        return abs(position)
if __name__== "__main__":
    a = Solution1()
    moves1 = "L_RL__R"
    print(a.furthestDistanceFromOrigin(moves1))  # 3

    moves2 = "_R__LL_"
    print(a.furthestDistanceFromOrigin(moves2))  # 5

    moves3 = "_______"
    print(a.furthestDistanceFromOrigin(moves3))  # 7
## Time Complexity: O(n) where n is the length of the input string moves. We need to iterate through the string once to calculate the position and maximum distance.
## Space Complexity: O(1) since we are using a constant amount of extra space to store the position and maximum distance.

