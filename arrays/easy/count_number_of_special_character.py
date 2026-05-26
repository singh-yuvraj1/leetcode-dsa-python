# 3120. Count the Number of Special Characters I
# Hint
# You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.
# Return the number of special letters in word.

# Example 1:
# Input: word = "aaAbcBC"
# Output: 3

# Explanation:
# The special characters in word are 'a', 'b', and 'c'.


# Example 2:
# Input: word = "abc"


# Output: 0
# Explanation:
# No character in word appears in uppercase.


# Example 3:
# Input: word = "abBCab"
# Output: 1

# Explanation:
# The only special character in word is 'b'.


# Constraints:
# 1 <= word.length <= 50
# word consists of only lowercase and uppercase English letters.


#solution 1--- Brute Force Solution --- Nested loops
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        
        count = 0

        for ch in "abcdefghijklmnopqrstuvwxyz":

            hasLower = False
            hasUpper = False

            for c in word:

                if c == ch:
                    hasLower = True

                if c == ch.upper():
                    hasUpper = True

            if hasLower and hasUpper:
                count += 1

        return count
if __name__ == "__main__":
    word = "aaAbcBC"
    print(Solution().numberOfSpecialChars(word))
#time complexity: O(n) where n is the length of the input string word.
#space complexity: O(1) since we are using a constant amount of extra space to store the count and the boolean variables.


#solution 2--- Using Sets
class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """

        lowerSet = set()
        upperSet = set()

        for c in word:

            if c.islower():
                lowerSet.add(c)

            else:
                upperSet.add(c)

        count = 0

        for ch in lowerSet:

            if ch.upper() in upperSet:
                count += 1

        return count
if __name__ == "__main__":
    word = "aaAbcBC"
    print(Solution().numberOfSpecialChars(word))
#time complexity: O(n) where n is the length of the input string word.
#space complexity: O(n) in the worst case, where n is the length of the input string word. This is because in the worst case, all characters in word could be unique, leading to a lowerSet and upperSet that each contain n/2 characters.
