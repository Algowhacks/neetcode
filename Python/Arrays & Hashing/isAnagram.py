# An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
# typically using all the original letters exactly once.

# Given two strings s and t, write a function to determine if t is an anagram of s.
# For example,
# s = "anagram", t = "nagaram", return true.
# s = "rat", t = "car", return false.


# Steps:
# 1. Compare the length of the two strings
# 2. If the length of the two strings are not equal, return False
# 3. Create a hash tables to store the characters of the strings
# 4. Loop through the length of the strings
# 5. If the character is in the hash table, increase the count of the character
# 6. Compare the two hash tables

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the length of the two strings are not the same, they cannot be anagrams
        if len(s) != len(t):
            return False

        # Create a hash tables to keep track of the characters in the string
        countS , countT = {}, {}
        # Iterate through the length of the string as we know they are the same length
        for i in range(len(s)):
            # Count the occurence of each character in the string (countS)
            countS[s[i]] = countS.get(s[i], 0) + 1 # get(key, default) returns the value associated with the key, or the default value if the key is not found
            countT[t[i]] = countT.get(t[i], 0) + 1

        # Compare the two hash tables to see if they are the same
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        # If they are the same, return True
        return True