# Given a string s, find the length of the longest substring without repeating characters.

# 1. Utilize a set to keep track of visited characters
# 2. Loop through the string, anytime we encounter a repeating char,
# we update our window, update the set
# Return the longest substring
# Exit

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # set to keep track of visited characters

        l = 0 # left pointer
        res = 0 # result

        for r in range(len(s)): # Start looping from the right
            while s[r] in charSet: # If the char is in the set, we update the window
                charSet.remove(s[l]) # Remove the leftmost char
                l +=1 # Update the left pointer
            charSet.add(s[r]) # Add the rightmost char
            res = max(res, r-l +1 ) # Update the result
        return res # Return the result


# test
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))




